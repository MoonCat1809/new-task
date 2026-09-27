package ssetcolor

import (
	"strings"
	"testing"
)

// Test 1: Basic wrap — red("hello") contains "hello", "[31m", "[0m"
func TestBasicWrap(t *testing.T) {
	result := Red("hello")
	if !strings.Contains(result, "hello") {
		t.Errorf("expected result to contain 'hello', got: %s", result)
	}
	if !strings.Contains(result, "[31m") {
		t.Errorf("expected result to contain '[31m', got: %s", result)
	}
	if !strings.Contains(result, "[0m") {
		t.Errorf("expected result to contain '[0m', got: %s", result)
	}
}

// Test 2: Multiple colors — different color codes (green, blue, etc.)
func TestMultipleColors(t *testing.T) {
	tests := []struct {
		name   string
		result string
		code   string
	}{
		{"green", Green("text"), "[32m"},
		{"blue", Blue("text"), "[34m"},
		{"yellow", Yellow("text"), "[33m"},
		{"cyan", Cyan("text"), "[36m"},
		{"magenta", Magenta("text"), "[35m"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if !strings.Contains(tt.result, tt.code) {
				t.Errorf("expected %s to contain %q, got: %s", tt.name, tt.code, tt.result)
			}
		})
	}
}

// Test 3: Style nesting — bold(red("inner")) contains [1m and [31m
func TestStyleNesting(t *testing.T) {
	result := Bold(Red("inner"))
	if !strings.Contains(result, "[1m") {
		t.Errorf("expected result to contain '[1m', got: %s", result)
	}
	if !strings.Contains(result, "[31m") {
		t.Errorf("expected result to contain '[31m', got: %s", result)
	}
	if !strings.Contains(result, "inner") {
		t.Errorf("expected result to contain 'inner', got: %s", result)
	}
}

// Test 4: 256-color — color_256("text", 208) contains "38;5;208"
func Test256Color(t *testing.T) {
	result := Color256("text", 208)
	if !strings.Contains(result, "38;5;208") {
		t.Errorf("expected result to contain '38;5;208', got: %s", result)
	}
	if !strings.Contains(result, "text") {
		t.Errorf("expected result to contain 'text', got: %s", result)
	}
}

// Test 5: TrueColor — color_rgb("text", 255, 100, 50) contains "38;2;255;100;50"
func TestTrueColor(t *testing.T) {
	result := ColorRGB("text", 255, 100, 50)
	if !strings.Contains(result, "38;2;255;100;50") {
		t.Errorf("expected result to contain '38;2;255;100;50', got: %s", result)
	}
	if !strings.Contains(result, "text") {
		t.Errorf("expected result to contain 'text', got: %s", result)
	}
}

// Test 6: Background — bg_red("text") contains "[41m"
func TestBackground(t *testing.T) {
	result := BgRed("text")
	if !strings.Contains(result, "[41m") {
		t.Errorf("expected result to contain '[41m', got: %s", result)
	}
	if !strings.Contains(result, "text") {
		t.Errorf("expected result to contain 'text', got: %s", result)
	}
}

// Test 7: Style builder — chainable builder produces combined ANSI codes
func TestStyleBuilder(t *testing.T) {
	s := NewStyle()
	defer s.Free()
	s.Bold().FG("red")
	result := s.Apply("hello")
	if !strings.Contains(result, "[1m") {
		t.Errorf("expected result to contain '[1m', got: %s", result)
	}
	if !strings.Contains(result, "[31m") {
		t.Errorf("expected result to contain '[31m', got: %s", result)
	}
	if !strings.Contains(result, "hello") {
		t.Errorf("expected result to contain 'hello', got: %s", result)
	}
	if !strings.Contains(result, "[0m") {
		t.Errorf("expected result to contain '[0m', got: %s", result)
	}
}

// Test 8: Strip ANSI — strip_ansi removes escape codes, leaves plain text
func TestStripANSI(t *testing.T) {
	colored := Red("hello")
	stripped := StripANSI(colored)
	if stripped != "hello" {
		t.Errorf("expected 'hello', got: %q", stripped)
	}
}

// Additional tests for bright colors, 256-color background, TrueColor background, style builder variants
func TestBrightColors(t *testing.T) {
	result := BrightRed("text")
	if !strings.Contains(result, "[91m") {
		t.Errorf("expected result to contain '[91m', got: %s", result)
	}
}

func TestBgBrightColors(t *testing.T) {
	result := BgBrightBlue("text")
	if !strings.Contains(result, "[104m") {
		t.Errorf("expected result to contain '[104m', got: %s", result)
	}
}

func TestBg256Color(t *testing.T) {
	result := BgColor256("text", 208)
	if !strings.Contains(result, "48;5;208") {
		t.Errorf("expected result to contain '48;5;208', got: %s", result)
	}
}

func TestBgTrueColor(t *testing.T) {
	result := BgColorRGB("text", 255, 100, 50)
	if !strings.Contains(result, "48;2;255;100;50") {
		t.Errorf("expected result to contain '48;2;255;100;50', got: %s", result)
	}
}

func TestStyleBuilderFG256(t *testing.T) {
	s := NewStyle()
	defer s.Free()
	s.Bold().FG256(208)
	result := s.Apply("hello")
	if !strings.Contains(result, "38;5;208") {
		t.Errorf("expected result to contain '38;5;208', got: %s", result)
	}
}

func TestStyleBuilderFGRGB(t *testing.T) {
	s := NewStyle()
	defer s.Free()
	s.Bold().FGRGB(255, 100, 50)
	result := s.Apply("hello")
	if !strings.Contains(result, "38;2;255;100;50") {
		t.Errorf("expected result to contain '38;2;255;100;50', got: %s", result)
	}
}

func TestStyleBuilderBG256(t *testing.T) {
	s := NewStyle()
	defer s.Free()
	s.Italic().BG256(129)
	result := s.Apply("hello")
	if !strings.Contains(result, "48;5;129") {
		t.Errorf("expected result to contain '48;5;129', got: %s", result)
	}
}

func TestStyleBuilderBGRGB(t *testing.T) {
	s := NewStyle()
	defer s.Free()
	s.Underline().BGRGB(100, 200, 50)
	result := s.Apply("hello")
	if !strings.Contains(result, "48;2;100;200;50") {
		t.Errorf("expected result to contain '48;2;100;200;50', got: %s", result)
	}
}

func TestSupportsColor(t *testing.T) {
	// Just verify it doesn't panic and returns a bool
	_ = SupportsColor()
}

func TestColorDepth(t *testing.T) {
	// Just verify it doesn't panic and returns an int
	depth := ColorDepth()
	if depth < 0 {
		t.Errorf("expected non-negative color depth, got: %d", depth)
	}
}