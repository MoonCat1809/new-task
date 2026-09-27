use ssetcolor::*;

#[test]
fn test_basic_wrap() {
    let result = red("hello");
    assert!(result.contains("hello"), "expected 'hello' in result");
    assert!(result.contains("[31m"), "expected '[31m' in result");
    assert!(result.contains("[0m"), "expected '[0m' in result");
}

#[test]
fn test_multiple_colors() {
    let tests = vec![
        ("green", green("text"), "[32m"),
        ("blue", blue("text"), "[34m"),
        ("yellow", yellow("text"), "[33m"),
        ("cyan", cyan("text"), "[36m"),
        ("magenta", magenta("text"), "[35m"),
    ];
    for (name, result, code) in tests {
        assert!(result.contains(code), "{} should contain {}", name, code);
    }
}

#[test]
fn test_style_nesting() {
    let result = bold(&red("inner"));
    assert!(result.contains("[1m"), "expected '[1m' in result");
    assert!(result.contains("[31m"), "expected '[31m' in result");
    assert!(result.contains("inner"), "expected 'inner' in result");
}

#[test]
fn test_256_color() {
    let result = color_256("text", 208);
    assert!(result.contains("38;5;208"), "expected '38;5;208' in result");
    assert!(result.contains("text"), "expected 'text' in result");
}

#[test]
fn test_truecolor() {
    let result = color_rgb("text", 255, 100, 50);
    assert!(result.contains("38;2;255;100;50"), "expected '38;2;255;100;50' in result");
    assert!(result.contains("text"), "expected 'text' in result");
}

#[test]
fn test_background() {
    let result = bg_red("text");
    assert!(result.contains("[41m"), "expected '[41m' in result");
    assert!(result.contains("text"), "expected 'text' in result");
}

#[test]
fn test_style_builder() {
    let s = Style::new().bold().fg("red");
    let result = s.apply("hello");
    assert!(result.contains("[1m"), "expected '[1m' in result");
    assert!(result.contains("[31m"), "expected '[31m' in result");
    assert!(result.contains("hello"), "expected 'hello' in result");
    assert!(result.contains("[0m"), "expected '[0m' in result");
}

#[test]
fn test_strip_ansi() {
    let colored = red("hello");
    let stripped = strip_ansi(&colored);
    assert_eq!(stripped, "hello", "expected 'hello', got: {:?}", stripped);
}

#[test]
fn test_bright_colors() {
    let result = bright_red("text");
    assert!(result.contains("[91m"), "expected '[91m' in result");
}

#[test]
fn test_bg_bright_colors() {
    let result = bg_bright_blue("text");
    assert!(result.contains("[104m"), "expected '[104m' in result");
}

#[test]
fn test_bg_256_color() {
    let result = bg_color_256("text", 208);
    assert!(result.contains("48;5;208"), "expected '48;5;208' in result");
}

#[test]
fn test_bg_truecolor() {
    let result = bg_color_rgb("text", 255, 100, 50);
    assert!(result.contains("48;2;255;100;50"), "expected '48;2;255;100;50' in result");
}

#[test]
fn test_style_builder_fg256() {
    let s = Style::new().bold().fg256(208);
    let result = s.apply("hello");
    assert!(result.contains("38;5;208"), "expected '38;5;208' in result");
}

#[test]
fn test_style_builder_fgrgb() {
    let s = Style::new().bold().fgrgb(255, 100, 50);
    let result = s.apply("hello");
    assert!(result.contains("38;2;255;100;50"), "expected '38;2;255;100;50' in result");
}

#[test]
fn test_style_builder_bg256() {
    let s = Style::new().italic().bg256(129);
    let result = s.apply("hello");
    assert!(result.contains("48;5;129"), "expected '48;5;129' in result");
}

#[test]
fn test_style_builder_bgrgb() {
    let s = Style::new().underline().bgrgb(100, 200, 50);
    let result = s.apply("hello");
    assert!(result.contains("48;2;100;200;50"), "expected '48;2;100;200;50' in result");
}

#[test]
fn test_supports_color() {
    let _ = supports_color();
}

#[test]
fn test_color_depth() {
    let depth = color_depth();
    assert!(depth > 0, "expected positive color depth");
}