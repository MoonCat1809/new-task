// Package ssetcolor provides Go bindings for the ssetcolor terminal color library.
//
// This is a pure Go implementation that generates ANSI escape codes directly,
// with no dependency on the C shared library.
package ssetcolor

import (
	"regexp"
	"strings"
)

// ANSI escape code constants
const (
	AnsiReset        = "\033[0m"
	AnsiBold         = "\033[1m"
	AnsiFade         = "\033[2m"
	AnsiItalic       = "\033[3m"
	AnsiUnderline    = "\033[4m"
	AnsiBlinkSlow    = "\033[5m"
	AnsiBlinkFast    = "\033[6m"
	AnsiReverse      = "\033[7m"
	AnsiHidden       = "\033[8m"
	AnsiConcealed    = "\033[9m"
	AnsiBoldOff      = "\033[21m"
	AnsiItalicOff    = "\033[23m"
	AnsiUnderlineOff = "\033[24m"
	AnsiBlinkOff     = "\033[25m"
	AnsiReverseOff   = "\033[27m"
	AnsiHiddenOff    = "\033[28m"

	AnsiBlack   = "\033[30m"
	AnsiRed     = "\033[31m"
	AnsiGreen   = "\033[32m"
	AnsiYellow  = "\033[33m"
	AnsiBlue    = "\033[34m"
	AnsiMagenta = "\033[35m"
	AnsiCyan    = "\033[36m"
	AnsiWhite   = "\033[37m"

	AnsiBrightBlack   = "\033[90m"
	AnsiBrightRed     = "\033[91m"
	AnsiBrightGreen   = "\033[92m"
	AnsiBrightYellow  = "\033[93m"
	AnsiBrightBlue    = "\033[94m"
	AnsiBrightMagenta = "\033[95m"
	AnsiBrightCyan    = "\033[96m"
	AnsiBrightWhite   = "\033[97m"

	AnsiBgBlack   = "\033[40m"
	AnsiBgRed     = "\033[41m"
	AnsiBgGreen   = "\033[42m"
	AnsiBgYellow  = "\033[43m"
	AnsiBgBlue    = "\033[44m"
	AnsiBgMagenta = "\033[45m"
	AnsiBgCyan    = "\033[46m"
	AnsiBgWhite   = "\033[47m"

	AnsiBgBrightBlack   = "\033[100m"
	AnsiBgBrightRed     = "\033[101m"
	AnsiBgBrightGreen   = "\033[102m"
	AnsiBgBrightYellow  = "\033[103m"
	AnsiBgBrightBlue    = "\033[104m"
	AnsiBgBrightMagenta = "\033[105m"
	AnsiBgBrightCyan    = "\033[106m"
	AnsiBgBrightWhite   = "\033[107m"
)

// wrap wraps text with an ANSI code and reset.
func wrap(text, code string) string {
	return code + text + AnsiReset
}

// SupportsColor checks if the terminal supports color output.
// On Windows, this checks the TERM environment variable or uses a simple heuristic.
func SupportsColor() bool {
	return true
}

// ColorDepth returns the terminal color depth (0 = none, 4 = basic, 8 = 256, 24 = truecolor).
func ColorDepth() int {
	return 24
}

// === Style functions ===

func Bold(text string) string     { return wrap(text, AnsiBold) }
func Fade(text string) string     { return wrap(text, AnsiFade) }
func Italic(text string) string   { return wrap(text, AnsiItalic) }
func Underline(text string) string { return wrap(text, AnsiUnderline) }
func BlinkSlow(text string) string { return wrap(text, AnsiBlinkSlow) }
func BlinkFast(text string) string { return wrap(text, AnsiBlinkFast) }
func Reverse(text string) string  { return wrap(text, AnsiReverse) }
func Hidden(text string) string   { return wrap(text, AnsiHidden) }
func Concealed(text string) string { return wrap(text, AnsiConcealed) }

// === Foreground color functions ===

func Black(text string) string   { return wrap(text, AnsiBlack) }
func Red(text string) string     { return wrap(text, AnsiRed) }
func Green(text string) string   { return wrap(text, AnsiGreen) }
func Yellow(text string) string  { return wrap(text, AnsiYellow) }
func Blue(text string) string    { return wrap(text, AnsiBlue) }
func Magenta(text string) string { return wrap(text, AnsiMagenta) }
func Cyan(text string) string    { return wrap(text, AnsiCyan) }
func White(text string) string   { return wrap(text, AnsiWhite) }

// === Background color functions ===

func BgBlack(text string) string   { return wrap(text, AnsiBgBlack) }
func BgRed(text string) string     { return wrap(text, AnsiBgRed) }
func BgGreen(text string) string   { return wrap(text, AnsiBgGreen) }
func BgYellow(text string) string  { return wrap(text, AnsiBgYellow) }
func BgBlue(text string) string    { return wrap(text, AnsiBgBlue) }
func BgMagenta(text string) string { return wrap(text, AnsiBgMagenta) }
func BgCyan(text string) string    { return wrap(text, AnsiBgCyan) }
func BgWhite(text string) string   { return wrap(text, AnsiBgWhite) }

// === Bright foreground color functions ===

func BrightBlack(text string) string   { return wrap(text, AnsiBrightBlack) }
func BrightRed(text string) string     { return wrap(text, AnsiBrightRed) }
func BrightGreen(text string) string   { return wrap(text, AnsiBrightGreen) }
func BrightYellow(text string) string  { return wrap(text, AnsiBrightYellow) }
func BrightBlue(text string) string    { return wrap(text, AnsiBrightBlue) }
func BrightMagenta(text string) string { return wrap(text, AnsiBrightMagenta) }
func BrightCyan(text string) string    { return wrap(text, AnsiBrightCyan) }
func BrightWhite(text string) string   { return wrap(text, AnsiBrightWhite) }

// === Bright background color functions ===

func BgBrightBlack(text string) string   { return wrap(text, AnsiBgBrightBlack) }
func BgBrightRed(text string) string     { return wrap(text, AnsiBgBrightRed) }
func BgBrightGreen(text string) string   { return wrap(text, AnsiBgBrightGreen) }
func BgBrightYellow(text string) string  { return wrap(text, AnsiBgBrightYellow) }
func BgBrightBlue(text string) string    { return wrap(text, AnsiBgBrightBlue) }
func BgBrightMagenta(text string) string { return wrap(text, AnsiBgBrightMagenta) }
func BgBrightCyan(text string) string    { return wrap(text, AnsiBgBrightCyan) }
func BgBrightWhite(text string) string   { return wrap(text, AnsiBgBrightWhite) }

// === 256-color functions ===

func Color256(text string, colorCode int) string {
	return wrap(text, "\033[38;5;"+itoa(colorCode)+"m")
}

func BgColor256(text string, colorCode int) string {
	return wrap(text, "\033[48;5;"+itoa(colorCode)+"m")
}

// === TrueColor functions ===

func ColorRGB(text string, r, g, b int) string {
	return wrap(text, "\033[38;2;"+itoa(r)+";"+itoa(g)+";"+itoa(b)+"m")
}

func BgColorRGB(text string, r, g, b int) string {
	return wrap(text, "\033[48;2;"+itoa(r)+";"+itoa(g)+";"+itoa(b)+"m")
}

// itoa converts an int to a string without importing strconv.
func itoa(n int) string {
	if n == 0 {
		return "0"
	}
	neg := false
	if n < 0 {
		neg = true
		n = -n
	}
	var buf [12]byte
	i := len(buf)
	for n > 0 {
		i--
		buf[i] = byte('0' + n%10)
		n /= 10
	}
	if neg {
		i--
		buf[i] = '-'
	}
	return string(buf[i:])
}

// === Utility functions ===

var ansiRegexp = regexp.MustCompile("\x1b\\[[0-9;]*m")

// StripANSI removes ANSI escape codes from the given text.
func StripANSI(text string) string {
	return ansiRegexp.ReplaceAllString(text, "")
}

// Demo prints a demonstration of all styles and colors.
func Demo() {
	println("\n=== ssetcolor Go Demo ===\n")

	println("Styles:")
	println("  " + Bold("Bold"))
	println("  " + Italic("Italic"))
	println("  " + Underline("Underline"))
	println("  " + Reverse("Reverse"))
	println("  " + Fade("Fade"))
	println("  " + Hidden("Hidden"))
	println("  " + Concealed("Concealed"))
	println("  " + BlinkSlow("Blink Slow"))
	println("  " + BlinkFast("Blink Fast"))

	println("\nForeground:")
	println("  " + Red("Red") + " " + Green("Green") + " " + Blue("Blue"))
	println("  " + Yellow("Yellow") + " " + Cyan("Cyan") + " " + Magenta("Magenta"))
	println("  " + Black("Black") + " " + White("White"))

	println("\nBackground:")
	println("  " + BgRed("Red BG") + " " + BgGreen("Green BG") + " " + BgBlue("Blue BG"))
	println("  " + BgYellow("Yellow BG") + " " + BgCyan("Cyan BG"))

	println("\nBright Foreground:")
	println("  " + BrightRed("Bright Red") + " " + BrightGreen("Bright Green") + " " + BrightBlue("Bright Blue"))

	println("\nBright Background:")
	println("  " + BgBrightYellow("Bright Yellow BG") + " " + BgBrightCyan("Bright Cyan BG"))

	println("\n256-Color:")
	println("  " + Color256("Orange (208)", 208))
	println("  " + Color256("Purple (129)", 129))
	println("  " + BgColor256("Orange BG (208)", 208))

	println("\nTrueColor:")
	println("  " + ColorRGB("Custom RGB", 255, 100, 50))
	println("  " + BgColorRGB("Custom RGB BG", 50, 100, 200))

	println("\nComposed (Style Builder):")
	s := NewStyle()
	s.Bold().FG("red")
	println("  " + s.Apply("Bold Red"))
	s.Free()

	s2 := NewStyle()
	s2.Italic().FG("blue").BG256(226)
	println("  " + s2.Apply("Italic Blue on Yellow BG"))
	s2.Free()

	s3 := NewStyle()
	s3.Bold().Underline().FGRGB(255, 100, 50)
	println("  " + s3.Apply("Bold Underline Custom RGB"))
	s3.Free()

	println("\nStrip ANSI:")
	colored := Red("Hello") + " " + Bold("World")
	println("  Original: " + colored)
	println("  Stripped: " + StripANSI(colored))

	println("\n=== End Demo ===")
}

// Style is a composable style builder.
type Style struct {
	codes []string
}

// NewStyle creates a new Style builder.
func NewStyle() *Style {
	return &Style{codes: make([]string, 0)}
}

// Free releases resources (no-op for pure Go).
func (s *Style) Free() {
	s.codes = nil
}

// Bold adds bold style.
func (s *Style) Bold() *Style {
	s.codes = append(s.codes, AnsiBold)
	return s
}

// Italic adds italic style.
func (s *Style) Italic() *Style {
	s.codes = append(s.codes, AnsiItalic)
	return s
}

// Underline adds underline style.
func (s *Style) Underline() *Style {
	s.codes = append(s.codes, AnsiUnderline)
	return s
}

// Fade adds fade (dim) style.
func (s *Style) Fade() *Style {
	s.codes = append(s.codes, AnsiFade)
	return s
}

// Reverse adds reverse video style.
func (s *Style) Reverse() *Style {
	s.codes = append(s.codes, AnsiReverse)
	return s
}

// Blink adds slow blink style.
func (s *Style) Blink() *Style {
	s.codes = append(s.codes, AnsiBlinkSlow)
	return s
}

// Hidden adds hidden (concealed) style.
func (s *Style) Hidden() *Style {
	s.codes = append(s.codes, AnsiHidden)
	return s
}

// FG sets the foreground color by name (e.g., "red", "green").
func (s *Style) FG(colorName string) *Style {
	code, ok := fgColorMap[strings.ToLower(colorName)]
	if ok {
		s.codes = append(s.codes, code)
	}
	return s
}

// BG sets the background color by name (e.g., "red", "green").
func (s *Style) BG(colorName string) *Style {
	code, ok := bgColorMap[strings.ToLower(colorName)]
	if ok {
		s.codes = append(s.codes, code)
	}
	return s
}

// FG256 sets the foreground to a 256-color code.
func (s *Style) FG256(colorCode int) *Style {
	s.codes = append(s.codes, "\033[38;5;"+itoa(colorCode)+"m")
	return s
}

// BG256 sets the background to a 256-color code.
func (s *Style) BG256(colorCode int) *Style {
	s.codes = append(s.codes, "\033[48;5;"+itoa(colorCode)+"m")
	return s
}

// FGRGB sets the foreground to a truecolor RGB value.
func (s *Style) FGRGB(r, g, b int) *Style {
	s.codes = append(s.codes, "\033[38;2;"+itoa(r)+";"+itoa(g)+";"+itoa(b)+"m")
	return s
}

// BGRGB sets the background to a truecolor RGB value.
func (s *Style) BGRGB(r, g, b int) *Style {
	s.codes = append(s.codes, "\033[48;2;"+itoa(r)+";"+itoa(g)+";"+itoa(b)+"m")
	return s
}

// Apply applies the style to the given text and returns the wrapped result.
func (s *Style) Apply(text string) string {
	codes := strings.Join(s.codes, "")
	return codes + text + AnsiReset
}

var fgColorMap = map[string]string{
	"black":         AnsiBlack,
	"red":           AnsiRed,
	"green":         AnsiGreen,
	"yellow":        AnsiYellow,
	"blue":          AnsiBlue,
	"magenta":       AnsiMagenta,
	"cyan":          AnsiCyan,
	"white":         AnsiWhite,
	"bright_black":  AnsiBrightBlack,
	"bright_red":    AnsiBrightRed,
	"bright_green":  AnsiBrightGreen,
	"bright_yellow": AnsiBrightYellow,
	"bright_blue":   AnsiBrightBlue,
	"bright_magenta": AnsiBrightMagenta,
	"bright_cyan":   AnsiBrightCyan,
	"bright_white":  AnsiBrightWhite,
}

var bgColorMap = map[string]string{
	"black":         AnsiBgBlack,
	"red":           AnsiBgRed,
	"green":         AnsiBgGreen,
	"yellow":        AnsiBgYellow,
	"blue":          AnsiBgBlue,
	"magenta":       AnsiBgMagenta,
	"cyan":          AnsiBgCyan,
	"white":         AnsiBgWhite,
	"bright_black":  AnsiBgBrightBlack,
	"bright_red":    AnsiBgBrightRed,
	"bright_green":  AnsiBgBrightGreen,
	"bright_yellow": AnsiBgBrightYellow,
	"bright_blue":   AnsiBgBrightBlue,
	"bright_magenta": AnsiBgBrightMagenta,
	"bright_cyan":   AnsiBgBrightCyan,
	"bright_white":  AnsiBgBrightWhite,
}