-- ssetcolor Lua tests
--
-- Run with:  luajit lua/test.lua
--
-- Covers the 8 test-matrix categories plus extras (bright colors, 256/TrueColor
-- backgrounds, style-builder variants).

-- Ensure the module in this directory can be required.
local dir = (arg and arg[0] and arg[0]:match("^(.*)[/\\]")) or "."
package.path = dir .. "/?.lua;" .. package.path

local ssc = require("ssetcolor")

local pass_count = 0
local fail_count = 0

local function check(condition, message)
    if condition then
        pass_count = pass_count + 1
        print("  PASS  " .. message)
    else
        fail_count = fail_count + 1
        print("  FAIL  " .. message)
    end
end

local function contains(haystack, needle)
    return haystack:find(needle, 1, true) ~= nil
end

print("\n=== ssetcolor Lua Tests ===\n")

-- Test 1: Basic wrap — red("hello") contains "hello", "[31m", "[0m"
print("Test 1: Basic wrap")
local t1 = ssc.red("hello")
check(contains(t1, "hello"), "red(\"hello\") contains 'hello'")
check(contains(t1, "[31m"), "red(\"hello\") contains '[31m'")
check(contains(t1, "[0m"), "red(\"hello\") contains '[0m'")

-- Test 2: Multiple colors — different color codes
print("Test 2: Multiple colors")
check(contains(ssc.green("text"), "[32m"), "green -> [32m")
check(contains(ssc.blue("text"), "[34m"), "blue -> [34m")
check(contains(ssc.yellow("text"), "[33m"), "yellow -> [33m")
check(contains(ssc.cyan("text"), "[36m"), "cyan -> [36m")
check(contains(ssc.magenta("text"), "[35m"), "magenta -> [35m")

-- Test 3: Style nesting — bold(red("inner")) contains [1m and [31m
print("Test 3: Style nesting")
local t3 = ssc.bold(ssc.red("inner"))
check(contains(t3, "[1m"), "contains '[1m'")
check(contains(t3, "[31m"), "contains '[31m'")
check(contains(t3, "inner"), "contains 'inner'")

-- Test 4: 256-color — color_256("text", 208) contains "38;5;208"
print("Test 4: 256-color")
local t4 = ssc.color_256("text", 208)
check(contains(t4, "38;5;208"), "contains '38;5;208'")
check(contains(t4, "text"), "contains 'text'")

-- Test 5: TrueColor — color_rgb("text", 255, 100, 50) contains "38;2;255;100;50"
print("Test 5: TrueColor")
local t5 = ssc.color_rgb("text", 255, 100, 50)
check(contains(t5, "38;2;255;100;50"), "contains '38;2;255;100;50'")
check(contains(t5, "text"), "contains 'text'")

-- Test 6: Background — bg_red("text") contains "[41m"
print("Test 6: Background")
local t6 = ssc.bg_red("text")
check(contains(t6, "[41m"), "contains '[41m'")
check(contains(t6, "text"), "contains 'text'")

-- Test 7: Style builder — chainable builder produces combined ANSI codes
print("Test 7: Style builder")
local s = ssc.style():bold():fg("red")
local t7 = s:apply("hello")
check(contains(t7, "[1m"), "contains '[1m'")
check(contains(t7, "[31m"), "contains '[31m'")
check(contains(t7, "hello"), "contains 'hello'")
check(contains(t7, "[0m"), "contains '[0m'")

-- Test 8: Strip ANSI — strip_ansi removes escape codes, leaves plain text
print("Test 8: Strip ANSI")
local colored = ssc.red("hello")
check(ssc.strip_ansi(colored) == "hello", "strip_ansi(red(\"hello\")) == 'hello'")

-- Extras
print("Extra tests")
check(contains(ssc.bright_red("text"), "[91m"), "bright_red -> [91m")
check(contains(ssc.bg_bright_blue("text"), "[104m"), "bg_bright_blue -> [104m")
check(contains(ssc.bg_color_256("text", 208), "48;5;208"), "bg_color_256 -> 48;5;208")
check(contains(ssc.bg_color_rgb("text", 255, 100, 50), "48;2;255;100;50"), "bg_color_rgb -> 48;2;255;100;50")

local s_fg256 = ssc.style():bold():fg256(208)
check(contains(s_fg256:apply("hello"), "38;5;208"), "style fg256 -> 38;5;208")
local s_fgrgb = ssc.style():bold():fgrgb(255, 100, 50)
check(contains(s_fgrgb:apply("hello"), "38;2;255;100;50"), "style fgrgb -> 38;2;255;100;50")
local s_bg256 = ssc.style():italic():bg256(129)
check(contains(s_bg256:apply("hello"), "48;5;129"), "style bg256 -> 48;5;129")
local s_bgrgb = ssc.style():underline():bgrgb(100, 200, 50)
check(contains(s_bgrgb:apply("hello"), "48;2;100;200;50"), "style bgrgb -> 48;2;100;200;50")

-- Utility functions should at least run without error.
local _ = ssc.supports_color()
local depth = ssc.color_depth()
check(type(depth) == "number" and depth > 0, "color_depth() is positive")

print("\n=== Results ===")
print(string.format("Passed: %d, Failed: %d", pass_count, fail_count))
if fail_count > 0 then
    os.exit(1)
else
    print("All tests passed!")
    os.exit(0)
end
