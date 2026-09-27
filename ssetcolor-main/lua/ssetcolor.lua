-- ssetcolor — Terminal color library (Lua bindings)
--
-- LuaJIT FFI module. Uses the compiled C shared library when available
-- (via ffi.cdef + ffi.load), and falls back to a pure Lua implementation so the
-- module remains fully usable even without the shared library.
--
-- Usage:
--   local ssetcolor = require("ssetcolor")
--   print(ssetcolor.bold(ssetcolor.red("Hello!")))
--   local s = ssetcolor.style():bold():fg("red")
--   print(s:apply("Styled text"))
--
-- Run:
--   luajit lua/demo.lua    (demo)
--   luajit lua/test.lua    (tests)

local M = {}

-- ============================================================================
-- LuaJIT FFI setup
-- ============================================================================

local has_ffi, ffi = pcall(require, "ffi")

local c = nil -- C library handle (nil when unavailable)
local C_AVAILABLE = false

if has_ffi then
    -- Declare the subset of the C API consumed through FFI.
    ffi.cdef[[
        int ssc_supports_color(void);
        int ssc_color_depth(void);

        char* ssc_wrap(const char* text, const char* ansi_code);
        char* ssc_strip_ansi(const char* text);
        void  ssc_free(char* ptr);
        void  ssc_demo(void);

        typedef struct ssc_style ssc_style_t;
        ssc_style_t* ssc_style_new(void);
        void ssc_style_free(ssc_style_t* style);
        void ssc_style_add(ssc_style_t* style, const char* ansi_code);
        void ssc_style_add_fg(ssc_style_t* style, const char* color_name);
        void ssc_style_add_bg(ssc_style_t* style, const char* color_name);
        void ssc_style_add_fg_256(ssc_style_t* style, int color_code);
        void ssc_style_add_bg_256(ssc_style_t* style, int color_code);
        void ssc_style_add_fg_rgb(ssc_style_t* style, int r, int g, int b);
        void ssc_style_add_bg_rgb(ssc_style_t* style, int r, int g, int b);
        char* ssc_style_apply(const ssc_style_t* style, const char* text);
    ]]

    local lib_name
    if ffi.os == "Windows" then
        lib_name = "ssetcolor"
    else
        lib_name = "libssetcolor"
    end

    local ok, lib = pcall(ffi.load, lib_name)
    if ok then
        c = lib
        C_AVAILABLE = true
    end
end

-- ============================================================================
-- ANSI escape code constants (also exposed on the module table)
-- ============================================================================

local RESET         = "\27[0m"
local BOLD          = "\27[1m"
local FADE          = "\27[2m"
local ITALIC        = "\27[3m"
local UNDERLINE     = "\27[4m"
local BLINK_SLOW    = "\27[5m"
local BLINK_FAST    = "\27[6m"
local REVERSE       = "\27[7m"
local HIDDEN        = "\27[8m"
local CONCEALED     = "\27[9m"

local BLACK   = "\27[30m"
local RED     = "\27[31m"
local GREEN   = "\27[32m"
local YELLOW  = "\27[33m"
local BLUE    = "\27[34m"
local MAGENTA = "\27[35m"
local CYAN    = "\27[36m"
local WHITE   = "\27[37m"

local BRIGHT_BLACK   = "\27[90m"
local BRIGHT_RED     = "\27[91m"
local BRIGHT_GREEN   = "\27[92m"
local BRIGHT_YELLOW  = "\27[93m"
local BRIGHT_BLUE    = "\27[94m"
local BRIGHT_MAGENTA = "\27[95m"
local BRIGHT_CYAN    = "\27[96m"
local BRIGHT_WHITE   = "\27[97m"

local BG_BLACK   = "\27[40m"
local BG_RED     = "\27[41m"
local BG_GREEN   = "\27[42m"
local BG_YELLOW  = "\27[43m"
local BG_BLUE    = "\27[44m"
local BG_MAGENTA = "\27[45m"
local BG_CYAN    = "\27[46m"
local BG_WHITE   = "\27[47m"

local BG_BRIGHT_BLACK   = "\27[100m"
local BG_BRIGHT_RED     = "\27[101m"
local BG_BRIGHT_GREEN   = "\27[102m"
local BG_BRIGHT_YELLOW  = "\27[103m"
local BG_BRIGHT_BLUE    = "\27[104m"
local BG_BRIGHT_MAGENTA = "\27[105m"
local BG_BRIGHT_CYAN    = "\27[106m"
local BG_BRIGHT_WHITE   = "\27[107m"

M.RESET         = RESET
M.BOLD          = BOLD
M.FADE          = FADE
M.ITALIC        = ITALIC
M.UNDERLINE     = UNDERLINE
M.BLINK_SLOW    = BLINK_SLOW
M.BLINK_FAST    = BLINK_FAST
M.REVERSE       = REVERSE
M.HIDDEN        = HIDDEN
M.CONCEALED     = CONCEALED
M.BLACK         = BLACK
M.RED           = RED
M.GREEN         = GREEN
M.YELLOW        = YELLOW
M.BLUE          = BLUE
M.MAGENTA       = MAGENTA
M.CYAN          = CYAN
M.WHITE         = WHITE
M.BRIGHT_BLACK  = BRIGHT_BLACK
M.BRIGHT_RED    = BRIGHT_RED
M.BRIGHT_GREEN  = BRIGHT_GREEN
M.BRIGHT_YELLOW = BRIGHT_YELLOW
M.BRIGHT_BLUE   = BRIGHT_BLUE
M.BRIGHT_MAGENTA= BRIGHT_MAGENTA
M.BRIGHT_CYAN   = BRIGHT_CYAN
M.BRIGHT_WHITE  = BRIGHT_WHITE
M.BG_BLACK      = BG_BLACK
M.BG_RED        = BG_RED
M.BG_GREEN      = BG_GREEN
M.BG_YELLOW     = BG_YELLOW
M.BG_BLUE       = BG_BLUE
M.BG_MAGENTA    = BG_MAGENTA
M.BG_CYAN       = BG_CYAN
M.BG_WHITE      = BG_WHITE
M.BG_BRIGHT_BLACK   = BG_BRIGHT_BLACK
M.BG_BRIGHT_RED     = BG_BRIGHT_RED
M.BG_BRIGHT_GREEN   = BG_BRIGHT_GREEN
M.BG_BRIGHT_YELLOW  = BG_BRIGHT_YELLOW
M.BG_BRIGHT_BLUE    = BG_BRIGHT_BLUE
M.BG_BRIGHT_MAGENTA = BG_BRIGHT_MAGENTA
M.BG_BRIGHT_CYAN    = BG_BRIGHT_CYAN
M.BG_BRIGHT_WHITE   = BG_BRIGHT_WHITE

-- ============================================================================
-- Internal helpers
-- ============================================================================

-- Wrap text with an ANSI code. Uses the C library when available, otherwise
-- builds the string in pure Lua.
local function wrap(text, code)
    if C_AVAILABLE and c and c.ssc_wrap then
        local ok, p = pcall(function() return c.ssc_wrap(text, code) end)
        if ok and p then
            local res
            local ok2, s = pcall(ffi.string, p)
            if ok2 then res = s end
            pcall(function() c.ssc_free(p) end)
            if res then return res end
        end
    end
    return code .. text .. RESET
end

-- Color lookup tables for the style builder.
local fg_names = {
    black = BLACK, red = RED, green = GREEN, yellow = YELLOW,
    blue = BLUE, magenta = MAGENTA, cyan = CYAN, white = WHITE,
    bright_black = BRIGHT_BLACK, bright_red = BRIGHT_RED,
    bright_green = BRIGHT_GREEN, bright_yellow = BRIGHT_YELLOW,
    bright_blue = BRIGHT_BLUE, bright_magenta = BRIGHT_MAGENTA,
    bright_cyan = BRIGHT_CYAN, bright_white = BRIGHT_WHITE,
}

local bg_names = {
    black = BG_BLACK, red = BG_RED, green = BG_GREEN, yellow = BG_YELLOW,
    blue = BG_BLUE, magenta = BG_MAGENTA, cyan = BG_CYAN, white = BG_WHITE,
    bright_black = BG_BRIGHT_BLACK, bright_red = BG_BRIGHT_RED,
    bright_green = BG_BRIGHT_GREEN, bright_yellow = BG_BRIGHT_YELLOW,
    bright_blue = BG_BRIGHT_BLUE, bright_magenta = BG_BRIGHT_MAGENTA,
    bright_cyan = BG_BRIGHT_CYAN, bright_white = BG_BRIGHT_WHITE,
}

-- ============================================================================
-- Style functions (9)
-- ============================================================================

function M.bold(text)      return wrap(text, BOLD) end
function M.fade(text)      return wrap(text, FADE) end
function M.italic(text)    return wrap(text, ITALIC) end
function M.underline(text) return wrap(text, UNDERLINE) end
function M.blink_slow(text) return wrap(text, BLINK_SLOW) end
function M.blink_fast(text) return wrap(text, BLINK_FAST) end
function M.reverse(text)   return wrap(text, REVERSE) end
function M.hidden(text)    return wrap(text, HIDDEN) end
function M.concealed(text) return wrap(text, CONCEALED) end

-- ============================================================================
-- Foreground color functions (8)
-- ============================================================================

function M.black(text)   return wrap(text, BLACK) end
function M.red(text)     return wrap(text, RED) end
function M.green(text)   return wrap(text, GREEN) end
function M.yellow(text)  return wrap(text, YELLOW) end
function M.blue(text)    return wrap(text, BLUE) end
function M.magenta(text) return wrap(text, MAGENTA) end
function M.cyan(text)    return wrap(text, CYAN) end
function M.white(text)   return wrap(text, WHITE) end

-- ============================================================================
-- Background color functions (8)
-- ============================================================================

function M.bg_black(text)   return wrap(text, BG_BLACK) end
function M.bg_red(text)     return wrap(text, BG_RED) end
function M.bg_green(text)   return wrap(text, BG_GREEN) end
function M.bg_yellow(text)  return wrap(text, BG_YELLOW) end
function M.bg_blue(text)    return wrap(text, BG_BLUE) end
function M.bg_magenta(text) return wrap(text, BG_MAGENTA) end
function M.bg_cyan(text)    return wrap(text, BG_CYAN) end
function M.bg_white(text)   return wrap(text, BG_WHITE) end

-- ============================================================================
-- Bright foreground color functions (8)
-- ============================================================================

function M.bright_black(text)   return wrap(text, BRIGHT_BLACK) end
function M.bright_red(text)     return wrap(text, BRIGHT_RED) end
function M.bright_green(text)   return wrap(text, BRIGHT_GREEN) end
function M.bright_yellow(text)  return wrap(text, BRIGHT_YELLOW) end
function M.bright_blue(text)    return wrap(text, BRIGHT_BLUE) end
function M.bright_magenta(text) return wrap(text, BRIGHT_MAGENTA) end
function M.bright_cyan(text)    return wrap(text, BRIGHT_CYAN) end
function M.bright_white(text)   return wrap(text, BRIGHT_WHITE) end

-- ============================================================================
-- Bright background color functions (8)
-- ============================================================================

function M.bg_bright_black(text)   return wrap(text, BG_BRIGHT_BLACK) end
function M.bg_bright_red(text)     return wrap(text, BG_BRIGHT_RED) end
function M.bg_bright_green(text)   return wrap(text, BG_BRIGHT_GREEN) end
function M.bg_bright_yellow(text)  return wrap(text, BG_BRIGHT_YELLOW) end
function M.bg_bright_blue(text)    return wrap(text, BG_BRIGHT_BLUE) end
function M.bg_bright_magenta(text) return wrap(text, BG_BRIGHT_MAGENTA) end
function M.bg_bright_cyan(text)    return wrap(text, BG_BRIGHT_CYAN) end
function M.bg_bright_white(text)   return wrap(text, BG_BRIGHT_WHITE) end

-- ============================================================================
-- 256-color functions
-- ============================================================================

function M.color_256(text, color_code)
    return wrap(text, string.format("\27[38;5;%dm", color_code))
end

function M.bg_color_256(text, color_code)
    return wrap(text, string.format("\27[48;5;%dm", color_code))
end

-- ============================================================================
-- TrueColor functions
-- ============================================================================

function M.color_rgb(text, r, g, b)
    return wrap(text, string.format("\27[38;2;%d;%d;%dm", r, g, b))
end

function M.bg_color_rgb(text, r, g, b)
    return wrap(text, string.format("\27[48;2;%d;%d;%dm", r, g, b))
end

-- ============================================================================
-- Style builder
-- ============================================================================

local Style = {}
Style.__index = Style

function Style:new()
    return setmetatable({ codes = {} }, Style)
end

function Style:bold()      table.insert(self.codes, BOLD); return self end
function Style:italic()    table.insert(self.codes, ITALIC); return self end
function Style:underline() table.insert(self.codes, UNDERLINE); return self end
function Style:fade()      table.insert(self.codes, FADE); return self end
function Style:reverse()   table.insert(self.codes, REVERSE); return self end
function Style:blink()     table.insert(self.codes, BLINK_SLOW); return self end
function Style:hidden()    table.insert(self.codes, HIDDEN); return self end

function Style:fg(name)
    local code = fg_names[name]
    if code then table.insert(self.codes, code) end
    return self
end

function Style:bg(name)
    local code = bg_names[name]
    if code then table.insert(self.codes, code) end
    return self
end

function Style:fg256(color_code)
    table.insert(self.codes, string.format("\27[38;5;%dm", color_code))
    return self
end

function Style:bg256(color_code)
    table.insert(self.codes, string.format("\27[48;5;%dm", color_code))
    return self
end

function Style:fgrgb(r, g, b)
    table.insert(self.codes, string.format("\27[38;2;%d;%d;%dm", r, g, b))
    return self
end

function Style:bgrgb(r, g, b)
    table.insert(self.codes, string.format("\27[48;2;%d;%d;%dm", r, g, b))
    return self
end

function Style:apply(text)
    return table.concat(self.codes, "") .. text .. RESET
end

-- Accessor matching the uppercase Style naming and Python `style`.
function M.style()
    return Style:new()
end

-- ============================================================================
-- Utility functions
-- ============================================================================

function M.supports_color()
    if C_AVAILABLE and c and c.ssc_supports_color then
        local ok, res = pcall(function() return c.ssc_supports_color() end)
        if ok then return res ~= 0 end
    end
    local term = os.getenv("TERM")
    if term == "dumb" then return false end
    return true
end

function M.color_depth()
    if C_AVAILABLE and c and c.ssc_color_depth then
        local ok, res = pcall(function() return c.ssc_color_depth() end)
        if ok then return res end
    end
    return 24 -- assume truecolor when no terminal detection available
end

function M.strip_ansi(text)
    if C_AVAILABLE and c and c.ssc_strip_ansi then
        local ok, p = pcall(function() return c.ssc_strip_ansi(text) end)
        if ok and p then
            local res
            local ok2, s = pcall(ffi.string, p)
            if ok2 then res = s end
            pcall(function() c.ssc_free(p) end)
            if res then return res end
        end
    end
    return (text:gsub("\27%[[0-9;]*m", ""))
end

function M.demo()
    if C_AVAILABLE and c and c.ssc_demo then
        local ok = pcall(function() return c.ssc_demo() end)
        if ok then return end
    end
    print("\n=== ssetcolor Lua Demo ===\n")
    print("Styles:")
    print("  " .. M.bold("Bold"))
    print("  " .. M.fade("Fade"))
    print("  " .. M.italic("Italic"))
    print("  " .. M.underline("Underline"))
    print("  " .. M.blink_slow("Blink Slow"))
    print("  " .. M.blink_fast("Blink Fast"))
    print("  " .. M.reverse("Reverse"))
    print("  " .. M.hidden("Hidden"))
    print("  " .. M.concealed("Concealed"))
    print("\nForeground:")
    print("  " .. M.red("Red") .. " " .. M.green("Green") .. " " .. M.blue("Blue"))
    print("  " .. M.yellow("Yellow") .. " " .. M.cyan("Cyan") .. " " .. M.magenta("Magenta"))
    print("  " .. M.black("Black") .. " " .. M.white("White"))
    print("\nBackground:")
    print("  " .. M.bg_red("Red BG") .. " " .. M.bg_green("Green BG") .. " " .. M.bg_blue("Blue BG"))
    print("  " .. M.bg_yellow("Yellow BG") .. " " .. M.bg_cyan("Cyan BG"))
    print("\nBright Foreground:")
    print("  " .. M.bright_red("Bright Red") .. " " .. M.bright_green("Bright Green") .. " " .. M.bright_blue("Bright Blue"))
    print("\nBright Background:")
    print("  " .. M.bg_bright_yellow("Bright Yellow BG") .. " " .. M.bg_bright_cyan("Bright Cyan BG"))
    print("\n256-Color:")
    print("  " .. M.color_256("Orange (208)", 208))
    print("  " .. M.color_256("Purple (129)", 129))
    print("  " .. M.bg_color_256("Orange BG (208)", 208))
    print("\nTrueColor:")
    print("  " .. M.color_rgb("Custom RGB", 255, 100, 50))
    print("  " .. M.bg_color_rgb("Custom RGB BG", 50, 100, 200))
    print("\nComposed (Style Builder):")
    local s = M.style():bold():fg("red")
    print("  " .. s:apply("Bold Red"))
    local s2 = M.style():italic():fg("blue"):bg256(226)
    print("  " .. s2:apply("Italic Blue on Yellow BG"))
    local s3 = M.style():bold():underline():fgrgb(255, 100, 50)
    print("  " .. s3:apply("Bold Underline Custom RGB"))
    print("\nStrip ANSI:")
    local colored = M.red("Hello") .. " " .. M.bold("World")
    print("  Original: " .. colored)
    print("  Stripped: " .. M.strip_ansi(colored))
    print("\n=== End Demo ===")
end

return M

