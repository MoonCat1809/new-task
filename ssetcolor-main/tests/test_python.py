"""Tests for ssetcolor Python bindings."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "python"))

from ssetcolor import (
    red, green, blue, bold, italic, underline,
    color_256, color_rgb, bg_red, bg_green, bg_blue,
    strip_ansi, style, RESET
)


def test_basic_wrap():
    result = red("hello")
    assert "hello" in result
    assert "[31m" in result
    assert "[0m" in result
    print("  PASS: test_basic_wrap")


def test_multiple_colors():
    result = green("green")
    assert "green" in result
    assert "[32m" in result
    print("  PASS: test_multiple_colors")


def test_style_nesting():
    inner = red("inner")
    outer = bold(inner)
    assert "inner" in outer
    assert "[31m" in outer
    assert "[1m" in outer
    print("  PASS: test_style_nesting")


def test_256_color():
    result = color_256("orange", 208)
    assert "orange" in result
    assert "38;5;208" in result
    print("  PASS: test_256_color")


def test_truecolor():
    result = color_rgb("custom", 255, 100, 50)
    assert "custom" in result
    assert "38;2;255;100;50" in result
    print("  PASS: test_truecolor")


def test_background():
    result = bg_red("bg")
    assert "bg" in result
    assert "[41m" in result
    print("  PASS: test_background")


def test_style_builder():
    s = style().bold().fg("red")
    result = s.apply("Bold Red")
    assert "Bold Red" in result
    assert "[1m" in result
    assert "[31m" in result
    print("  PASS: test_style_builder")


def test_strip_ansi():
    result = strip_ansi("\033[31mtext\033[0m")
    assert result == "text"
    print("  PASS: test_strip_ansi")


if __name__ == "__main__":
    print("\n=== ssetcolor Python Tests ===\n")
    test_basic_wrap()
    test_multiple_colors()
    test_style_nesting()
    test_256_color()
    test_truecolor()
    test_background()
    test_style_builder()
    test_strip_ansi()
    print("\nAll tests passed!\n")
