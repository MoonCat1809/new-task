#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "ssetcolor.h"

int tests_passed = 0;
int tests_failed = 0;

#define TEST(name, expr) do { \
    if (expr) { \
        tests_passed++; \
        printf("  PASS: %s\n", name); \
    } else { \
        tests_failed++; \
        printf("  FAIL: %s\n", name); \
    } \
} while(0)

int main(void) {
    printf("\n=== ssetcolor C Tests ===\n\n");

    // Test basic wrap
    char buf[256];
    int n = ssc_wrap_buf(buf, sizeof(buf), "hello", SSC_RED);
    TEST("wrap returns proper length", n > 5);
    TEST("wrap contains text", strstr(buf, "hello") != NULL);
    TEST("wrap contains reset", strstr(buf, "[0m") != NULL);
    TEST("wrap contains red code", strstr(buf, "[31m") != NULL);

    // Test style builder
    ssc_style_t* st = ssc_style_new();
    TEST("style_new not NULL", st != NULL);
    ssc_style_add_fg(st, "red");
    ssc_style_add(st, SSC_BOLD);
    char* result = ssc_style_apply(st, "styled");
    TEST("style_apply not NULL", result != NULL);
    TEST("style_apply contains text", strstr(result, "styled") != NULL);
    TEST("style_apply contains reset", strstr(result, "[0m") != NULL);
    TEST("style_apply contains bold", strstr(result, "[1m") != NULL);
    TEST("style_apply contains red", strstr(result, "[31m") != NULL);
    ssc_free(result);

    // Test 256-color
    result = ssc_color_256("text256", 208);
    TEST("color_256 not NULL", result != NULL);
    TEST("color_256 contains 38;5", strstr(result, "38;5;208") != NULL);
    ssc_free(result);

    // Test truecolor
    result = ssc_color_rgb("rgbtext", 255, 100, 50);
    TEST("color_rgb not NULL", result != NULL);
    TEST("color_rgb contains 38;2", strstr(result, "38;2;255;100;50") != NULL);
    ssc_free(result);

    // Test background
    result = ssc_bg_blue("bgblue");
    TEST("bg_blue not NULL", result != NULL);
    TEST("bg_blue contains 44m", strstr(result, "[44m") != NULL);
    ssc_free(result);

    // Test bright colors
    result = ssc_bright_red("bright");
    TEST("bright_red not NULL", result != NULL);
    TEST("bright_red contains 91m", strstr(result, "[91m") != NULL);
    ssc_free(result);

    // Test strip ANSI
    char* stripped = ssc_strip_ansi("\033[31mtext\033[0m");
    TEST("strip_ansi not NULL", stripped != NULL);
    TEST("strip_ansi removes codes", strcmp(stripped, "text") == 0);
    ssc_free(stripped);

    // Test terminal detection (may fail in CI, but should run)
    int sc = ssc_supports_color();
    int cd = ssc_color_depth();
    printf("  INFO: supports_color=%d, color_depth=%d\n", sc, cd);

    ssc_style_free(st);

    printf("\n=== Results: %d passed, %d failed ===\n\n", tests_passed, tests_failed);
    return tests_failed > 0 ? 1 : 0;
}
