"use strict";

// ssetcolor Node.js tests
//
// Run with: node test.js   (or: npm test)
//
// Covers the 8 test-matrix categories plus extras (bright colors, 256/TrueColor
// backgrounds, style-builder variants).

const ssc = require("./ssetcolor");

let pass = 0;
let fail = 0;

function check(cond, message) {
  if (cond) {
    pass++;
    console.log("  PASS  " + message);
  } else {
    fail++;
    console.log("  FAIL  " + message);
  }
}

function contains(haystack, needle) {
  return haystack.includes(needle);
}

console.log("\n=== ssetcolor Node.js Tests ===\n");

// Test 1: Basic wrap — red("hello") contains "hello", "[31m", "[0m"
console.log("Test 1: Basic wrap");
const t1 = ssc.red("hello");
check(contains(t1, "hello"), "red(\"hello\") contains 'hello'");
check(contains(t1, "[31m"), "red(\"hello\") contains '[31m'");
check(contains(t1, "[0m"), "red(\"hello\") contains '[0m'");

// Test 2: Multiple colors — different color codes
console.log("Test 2: Multiple colors");
check(contains(ssc.green("text"), "[32m"), "green -> [32m");
check(contains(ssc.blue("text"), "[34m"), "blue -> [34m");
check(contains(ssc.yellow("text"), "[33m"), "yellow -> [33m");
check(contains(ssc.cyan("text"), "[36m"), "cyan -> [36m");
check(contains(ssc.magenta("text"), "[35m"), "magenta -> [35m");

// Test 3: Style nesting — bold(red("inner")) contains [1m and [31m
console.log("Test 3: Style nesting");
const t3 = ssc.bold(ssc.red("inner"));
check(contains(t3, "[1m"), "contains '[1m'");
check(contains(t3, "[31m"), "contains '[31m'");
check(contains(t3, "inner"), "contains 'inner'");

// Test 4: 256-color — color256("text", 208) contains "38;5;208"
console.log("Test 4: 256-color");
const t4 = ssc.color256("text", 208);
check(contains(t4, "38;5;208"), "contains '38;5;208'");
check(contains(t4, "text"), "contains 'text'");

// Test 5: TrueColor — colorRgb("text", 255, 100, 50) contains "38;2;255;100;50"
console.log("Test 5: TrueColor");
const t5 = ssc.colorRgb("text", 255, 100, 50);
check(contains(t5, "38;2;255;100;50"), "contains '38;2;255;100;50'");
check(contains(t5, "text"), "contains 'text'");

// Test 6: Background — bgRed("text") contains "[41m"
console.log("Test 6: Background");
const t6 = ssc.bgRed("text");
check(contains(t6, "[41m"), "contains '[41m'");
check(contains(t6, "text"), "contains 'text'");

// Test 7: Style builder — chainable builder produces combined ANSI codes
console.log("Test 7: Style builder");
const t7 = ssc.style().bold().fg("red").apply("hello");
check(contains(t7, "[1m"), "contains '[1m'");
check(contains(t7, "[31m"), "contains '[31m'");
check(contains(t7, "hello"), "contains 'hello'");
check(contains(t7, "[0m"), "contains '[0m'");

// Test 8: Strip ANSI — stripAnsi removes escape codes, leaves plain text
console.log("Test 8: Strip ANSI");
check(ssc.stripAnsi(ssc.red("hello")) === "hello", "stripAnsi(red(\"hello\")) === 'hello'");

// Extras
console.log("Extra tests");
check(contains(ssc.brightRed("text"), "[91m"), "brightRed -> [91m");
check(contains(ssc.bgBrightBlue("text"), "[104m"), "bgBrightBlue -> [104m");
check(contains(ssc.bgColor256("text", 208), "48;5;208"), "bgColor256 -> 48;5;208");
check(contains(ssc.bgColorRgb("text", 255, 100, 50), "48;2;255;100;50"), "bgColorRgb -> 48;2;255;100;50");
check(contains(ssc.style().bold().fg256(208).apply("hello"), "38;5;208"), "style fg256 -> 38;5;208");
check(contains(ssc.style().bold().fgrgb(255, 100, 50).apply("hello"), "38;2;255;100;50"), "style fgrgb -> 38;2;255;100;50");
check(contains(ssc.style().italic().bg256(129).apply("hello"), "48;5;129"), "style bg256 -> 48;5;129");
check(contains(ssc.style().underline().bgrgb(100, 200, 50).apply("hello"), "48;2;100;200;50"), "style bgrgb -> 48;2;100;200;50");

// Utility functions should at least run without error.
const _ = ssc.supportsColor();
const depth = ssc.colorDepth();
check(typeof depth === "number" && depth > 0, "colorDepth() is positive");

console.log("\n=== Results ===");
console.log("Passed: " + pass + ", Failed: " + fail);
if (fail > 0) {
  process.exit(1);
}
console.log("All tests passed!");
process.exit(0);
