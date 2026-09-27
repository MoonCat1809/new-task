package main

import (
	"fmt"

	"github.com/Anen135/ssetcolor/go"
)

func main() {
	fmt.Println("=== ssetcolor Go Demo ===")
	fmt.Println()

	fmt.Println("Styles:")
	fmt.Printf("  %s\n", ssetcolor.Bold("Bold"))
	fmt.Printf("  %s\n", ssetcolor.Italic("Italic"))
	fmt.Printf("  %s\n", ssetcolor.Underline("Underline"))
	fmt.Printf("  %s\n", ssetcolor.Reverse("Reverse"))
	fmt.Printf("  %s\n", ssetcolor.Fade("Fade"))
	fmt.Printf("  %s\n", ssetcolor.Hidden("Hidden"))
	fmt.Printf("  %s\n", ssetcolor.Concealed("Concealed"))
	fmt.Printf("  %s\n", ssetcolor.BlinkSlow("Blink Slow"))
	fmt.Printf("  %s\n", ssetcolor.BlinkFast("Blink Fast"))

	fmt.Println("\nForeground:")
	fmt.Printf("  %s %s %s\n", ssetcolor.Red("Red"), ssetcolor.Green("Green"), ssetcolor.Blue("Blue"))
	fmt.Printf("  %s %s %s\n", ssetcolor.Yellow("Yellow"), ssetcolor.Cyan("Cyan"), ssetcolor.Magenta("Magenta"))
	fmt.Printf("  %s %s\n", ssetcolor.Black("Black"), ssetcolor.White("White"))

	fmt.Println("\nBackground:")
	fmt.Printf("  %s %s %s\n", ssetcolor.BgRed("Red BG"), ssetcolor.BgGreen("Green BG"), ssetcolor.BgBlue("Blue BG"))
	fmt.Printf("  %s %s\n", ssetcolor.BgYellow("Yellow BG"), ssetcolor.BgCyan("Cyan BG"))

	fmt.Println("\nBright Foreground:")
	fmt.Printf("  %s %s %s\n", ssetcolor.BrightRed("Bright Red"), ssetcolor.BrightGreen("Bright Green"), ssetcolor.BrightBlue("Bright Blue"))

	fmt.Println("\nBright Background:")
	fmt.Printf("  %s %s\n", ssetcolor.BgBrightYellow("Bright Yellow BG"), ssetcolor.BgBrightCyan("Bright Cyan BG"))

	fmt.Println("\n256-Color:")
	fmt.Printf("  %s\n", ssetcolor.Color256("Orange (208)", 208))
	fmt.Printf("  %s\n", ssetcolor.Color256("Purple (129)", 129))
	fmt.Printf("  %s\n", ssetcolor.BgColor256("Orange BG (208)", 208))

	fmt.Println("\nTrueColor:")
	fmt.Printf("  %s\n", ssetcolor.ColorRGB("Custom RGB", 255, 100, 50))
	fmt.Printf("  %s\n", ssetcolor.BgColorRGB("Custom RGB BG", 50, 100, 200))

	fmt.Println("\nComposed (Style Builder):")
	s := ssetcolor.NewStyle()
	s.Bold().FG("red")
	fmt.Printf("  %s\n", s.Apply("Bold Red"))
	s.Free()

	s2 := ssetcolor.NewStyle()
	s2.Italic().FG("blue").BG256(226)
	fmt.Printf("  %s\n", s2.Apply("Italic Blue on Yellow BG"))
	s2.Free()

	s3 := ssetcolor.NewStyle()
	s3.Bold().Underline().FGRGB(255, 100, 50)
	fmt.Printf("  %s\n", s3.Apply("Bold Underline Custom RGB"))
	s3.Free()

	fmt.Println("\nStrip ANSI:")
	colored := ssetcolor.Red("Hello") + " " + ssetcolor.Bold("World")
	fmt.Printf("  Original: %s\n", colored)
	fmt.Printf("  Stripped: %s\n", ssetcolor.StripANSI(colored))

	fmt.Println("\n=== End Demo ===")
}