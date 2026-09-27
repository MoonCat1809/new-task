"use strict";

// ssetcolor — Terminal color library (Node.js bindings)
//
// Pure JavaScript implementation that generates ANSI escape codes directly.
// No native dependencies required.
//
// Usage:
//   const ssc = require("./ssetcolor");
//   console.log(ssc.bold(ssc.red("Hello!")));
//   const s = ssc.style().bold().fg("red");
//   console.log(s.apply("Styled text"));
//
// Run tests with `node test.js`, demo with `node demo.js`.

// ---- ANSI escape code constants (also exported) ----
const RESET         = "\x1b[0m";
const BOLD          = "\x1b[1m";
const FADE          = "\x1b[2m";
const ITALIC        = "\x1b[3m";
const UNDERLINE     = "\x1b[4m";
const BLINK_SLOW    = "\x1b[5m";
const BLINK_FAST    = "\x1b[6m";
const REVERSE       = "\x1b[7m";
const HIDDEN        = "\x1b[8m";
const CONCEALED     = "\x1b[9m";

const BLACK   = "\x1b[30m";
const RED     = "\x1b[31m";
const GREEN   = "\x1b[32m";
const YELLOW  = "\x1b[33m";
const BLUE    = "\x1b[34m";
const MAGENTA = "\x1b[35m";
const CYAN    = "\x1b[36m";
const WHITE   = "\x1b[37m";

const BRIGHT_BLACK   = "\x1b[90m";
const BRIGHT_RED     = "\x1b[91m";
const BRIGHT_GREEN   = "\x1b[92m";
const BRIGHT_YELLOW  = "\x1b[93m";
const BRIGHT_BLUE    = "\x1b[94m";
const BRIGHT_MAGENTA = "\x1b[95m";
const BRIGHT_CYAN    = "\x1b[96m";
const BRIGHT_WHITE   = "\x1b[97m";

const BG_BLACK   = "\x1b[40m";
const BG_RED     = "\x1b[41m";
const BG_GREEN   = "\x1b[42m";
const BG_YELLOW  = "\x1b[43m";
const BG_BLUE    = "\x1b[44m";
const BG_MAGENTA = "\x1b[45m";
const BG_CYAN    = "\x1b[46m";
const BG_WHITE   = "\x1b[47m";

const BG_BRIGHT_BLACK   = "\x1b[100m";
const BG_BRIGHT_RED     = "\x1b[101m";
const BG_BRIGHT_GREEN   = "\x1b[102m";
const BG_BRIGHT_YELLOW  = "\x1b[103m";
const BG_BRIGHT_BLUE    = "\x1b[104m";
const BG_BRIGHT_MAGENTA = "\x1b[105m";
const BG_BRIGHT_CYAN    = "\x1b[106m";
const BG_BRIGHT_WHITE   = "\x1b[107m";

// Color lookup tables for the style builder.
const FG_COLORS = {
  black: BLACK, red: RED, green: GREEN, yellow: YELLOW,
  blue: BLUE, magenta: MAGENTA, cyan: CYAN, white: WHITE,
  bright_black: BRIGHT_BLACK, bright_red: BRIGHT_RED,
  bright_green: BRIGHT_GREEN, bright_yellow: BRIGHT_YELLOW,
  bright_blue: BRIGHT_BLUE, bright_magenta: BRIGHT_MAGENTA,
  bright_cyan: BRIGHT_CYAN, bright_white: BRIGHT_WHITE,
};

const BG_COLORS = {
  black: BG_BLACK, red: BG_RED, green: BG_GREEN, yellow: BG_YELLOW,
  blue: BG_BLUE, magenta: BG_MAGENTA, cyan: BG_CYAN, white: BG_WHITE,
  bright_black: BG_BRIGHT_BLACK, bright_red: BG_BRIGHT_RED,
  bright_green: BG_BRIGHT_GREEN, bright_yellow: BG_BRIGHT_YELLOW,
  bright_blue: BG_BRIGHT_BLUE, bright_magenta: BG_BRIGHT_MAGENTA,
  bright_cyan: BG_BRIGHT_CYAN, bright_white: BG_BRIGHT_WHITE,
};

function wrap(text, code) {
  return code + text + RESET;
}

// ---- Style functions (9) ----
function bold(text)      { return wrap(text, BOLD); }
function fade(text)      { return wrap(text, FADE); }
function italic(text)    { return wrap(text, ITALIC); }
function underline(text) { return wrap(text, UNDERLINE); }
function blinkSlow(text) { return wrap(text, BLINK_SLOW); }
function blinkFast(text) { return wrap(text, BLINK_FAST); }
function reverse(text)   { return wrap(text, REVERSE); }
function hidden(text)    { return wrap(text, HIDDEN); }
function concealed(text) { return wrap(text, CONCEALED); }

// ---- Foreground color functions (8) ----
function black(text)   { return wrap(text, BLACK); }
function red(text)     { return wrap(text, RED); }
function green(text)   { return wrap(text, GREEN); }
function yellow(text)  { return wrap(text, YELLOW); }
function blue(text)    { return wrap(text, BLUE); }
function magenta(text) { return wrap(text, MAGENTA); }
function cyan(text)    { return wrap(text, CYAN); }
function white(text)   { return wrap(text, WHITE); }

// ---- Background color functions (8) ----
function bgBlack(text)   { return wrap(text, BG_BLACK); }
function bgRed(text)     { return wrap(text, BG_RED); }
function bgGreen(text)   { return wrap(text, BG_GREEN); }
function bgYellow(text)  { return wrap(text, BG_YELLOW); }
function bgBlue(text)    { return wrap(text, BG_BLUE); }
function bgMagenta(text) { return wrap(text, BG_MAGENTA); }
function bgCyan(text)    { return wrap(text, BG_CYAN); }
function bgWhite(text)   { return wrap(text, BG_WHITE); }

// ---- Bright foreground color functions (8) ----
function brightBlack(text)   { return wrap(text, BRIGHT_BLACK); }
function brightRed(text)     { return wrap(text, BRIGHT_RED); }
function brightGreen(text)   { return wrap(text, BRIGHT_GREEN); }
function brightYellow(text)  { return wrap(text, BRIGHT_YELLOW); }
function brightBlue(text)    { return wrap(text, BRIGHT_BLUE); }
function brightMagenta(text) { return wrap(text, BRIGHT_MAGENTA); }
function brightCyan(text)    { return wrap(text, BRIGHT_CYAN); }
function brightWhite(text)   { return wrap(text, BRIGHT_WHITE); }

// ---- Bright background color functions (8) ----
function bgBrightBlack(text)   { return wrap(text, BG_BRIGHT_BLACK); }
function bgBrightRed(text)     { return wrap(text, BG_BRIGHT_RED); }
function bgBrightGreen(text)   { return wrap(text, BG_BRIGHT_GREEN); }
function bgBrightYellow(text)  { return wrap(text, BG_BRIGHT_YELLOW); }
function bgBrightBlue(text)    { return wrap(text, BG_BRIGHT_BLUE); }
function bgBrightMagenta(text) { return wrap(text, BG_BRIGHT_MAGENTA); }
function bgBrightCyan(text)    { return wrap(text, BG_BRIGHT_CYAN); }
function bgBrightWhite(text)   { return wrap(text, BG_BRIGHT_WHITE); }

// ---- 256-color functions ----
function color256(text, code)   { return wrap(text, `\x1b[38;5;${code}m`); }
function bgColor256(text, code) { return wrap(text, `\x1b[48;5;${code}m`); }

// ---- TrueColor functions ----
function colorRgb(text, r, g, b)   { return wrap(text, `\x1b[38;2;${r};${g};${b}m`); }
function bgColorRgb(text, r, g, b) { return wrap(text, `\x1b[48;2;${r};${g};${b}m`); }

// ---- Style builder ----
class Style {
  constructor() { this.codes = []; }
  bold()      { this.codes.push(BOLD); return this; }
  italic()    { this.codes.push(ITALIC); return this; }
  underline() { this.codes.push(UNDERLINE); return this; }
  fade()      { this.codes.push(FADE); return this; }
  reverse()   { this.codes.push(REVERSE); return this; }
  blink()     { this.codes.push(BLINK_SLOW); return this; }
  hidden()    { this.codes.push(HIDDEN); return this; }
  fg(name)    { const code = FG_COLORS[name]; if (code) this.codes.push(code); return this; }
  bg(name)    { const code = BG_COLORS[name]; if (code) this.codes.push(code); return this; }
  fg256(code) { this.codes.push(`\x1b[38;5;${code}m`); return this; }
  bg256(code) { this.codes.push(`\x1b[48;5;${code}m`); return this; }
  fgrgb(r, g, b) { this.codes.push(`\x1b[38;2;${r};${g};${b}m`); return this; }
  bgrgb(r, g, b) { this.codes.push(`\x1b[48;2;${r};${g};${b}m`); return this; }
  apply(text) { return this.codes.join("") + text + RESET; }
}

function style() { return new Style(); }

// ---- Utility functions ----
function supportsColor() {
  if (process.env.NO_COLOR) return false;
  if (process.env.TERM === "dumb") return false;
  return true;
}

function colorDepth() { return 24; }

function stripAnsi(text) {
  return text.replace(/\x1b\[[0-9;]*m/g, "");
}

function demo() {
  console.log("\n=== ssetcolor Node.js Demo ===\n");
  console.log("Styles:");
  console.log("  " + bold("Bold"));
  console.log("  " + fade("Fade"));
  console.log("  " + italic("Italic"));
  console.log("  " + underline("Underline"));
  console.log("  " + blinkSlow("Blink Slow"));
  console.log("  " + blinkFast("Blink Fast"));
  console.log("  " + reverse("Reverse"));
  console.log("  " + hidden("Hidden"));
  console.log("  " + concealed("Concealed"));
  console.log("\nForeground:");
  console.log("  " + red("Red") + " " + green("Green") + " " + blue("Blue"));
  console.log("  " + yellow("Yellow") + " " + cyan("Cyan") + " " + magenta("Magenta"));
  console.log("  " + black("Black") + " " + white("White"));
  console.log("\nBackground:");
  console.log("  " + bgRed("Red BG") + " " + bgGreen("Green BG") + " " + bgBlue("Blue BG"));
  console.log("  " + bgYellow("Yellow BG") + " " + bgCyan("Cyan BG"));
  console.log("\nBright Foreground:");
  console.log("  " + brightRed("Bright Red") + " " + brightGreen("Bright Green") + " " + brightBlue("Bright Blue"));
  console.log("\nBright Background:");
  console.log("  " + bgBrightYellow("Bright Yellow BG") + " " + bgBrightCyan("Bright Cyan BG"));
  console.log("\n256-Color:");
  console.log("  " + color256("Orange (208)", 208));
  console.log("  " + color256("Purple (129)", 129));
  console.log("  " + bgColor256("Orange BG (208)", 208));
  console.log("\nTrueColor:");
  console.log("  " + colorRgb("Custom RGB", 255, 100, 50));
  console.log("  " + bgColorRgb("Custom RGB BG", 50, 100, 200));
  console.log("\nComposed (Style Builder):");
  console.log("  " + style().bold().fg("red").apply("Bold Red"));
  console.log("  " + style().italic().fg("blue").bg256(226).apply("Italic Blue on Yellow BG"));
  console.log("  " + style().bold().underline().fgrgb(255, 100, 50).apply("Bold Underline Custom RGB"));
  console.log("\nStrip ANSI:");
  const colored = red("Hello") + " " + bold("World");
  console.log("  Original: " + colored);
  console.log("  Stripped: " + stripAnsi(colored));
  console.log("\n=== End Demo ===");
}

module.exports = {
  RESET, BOLD, FADE, ITALIC, UNDERLINE, BLINK_SLOW, BLINK_FAST, REVERSE, HIDDEN, CONCEALED,
  BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
  BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE,
  BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE,
  BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_BLUE, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE,
  bold, fade, italic, underline, blinkSlow, blinkFast, reverse, hidden, concealed,
  black, red, green, yellow, blue, magenta, cyan, white,
  bgBlack, bgRed, bgGreen, bgYellow, bgBlue, bgMagenta, bgCyan, bgWhite,
  brightBlack, brightRed, brightGreen, brightYellow, brightBlue, brightMagenta, brightCyan, brightWhite,
  bgBrightBlack, bgBrightRed, bgBrightGreen, bgBrightYellow, bgBrightBlue, bgBrightMagenta, bgBrightCyan, bgBrightWhite,
  color256, bgColor256, colorRgb, bgColorRgb,
  style, Style,
  supportsColor, colorDepth, stripAnsi, demo,
};
