use ssetcolor::*;

fn main() {
    println!("=== ssetcolor Rust Demo ===");
    println!();

    println!("Styles:");
    println!("  {}", bold("Bold"));
    println!("  {}", italic("Italic"));
    println!("  {}", underline("Underline"));
    println!("  {}", reverse("Reverse"));
    println!("  {}", fade("Fade"));
    println!("  {}", hidden("Hidden"));
    println!("  {}", concealed("Concealed"));
    println!("  {}", blink_slow("Blink Slow"));
    println!("  {}", blink_fast("Blink Fast"));

    println!("\nForeground:");
    println!("  {} {} {}", red("Red"), green("Green"), blue("Blue"));
    println!("  {} {} {}", yellow("Yellow"), cyan("Cyan"), magenta("Magenta"));
    println!("  {} {}", black("Black"), white("White"));

    println!("\nBackground:");
    println!("  {} {} {}", bg_red("Red BG"), bg_green("Green BG"), bg_blue("Blue BG"));
    println!("  {} {}", bg_yellow("Yellow BG"), bg_cyan("Cyan BG"));

    println!("\nBright Foreground:");
    println!("  {} {} {}", bright_red("Bright Red"), bright_green("Bright Green"), bright_blue("Bright Blue"));

    println!("\nBright Background:");
    println!("  {} {}", bg_bright_yellow("Bright Yellow BG"), bg_bright_cyan("Bright Cyan BG"));

    println!("\n256-Color:");
    println!("  {}", color_256("Orange (208)", 208));
    println!("  {}", color_256("Purple (129)", 129));
    println!("  {}", bg_color_256("Orange BG (208)", 208));

    println!("\nTrueColor:");
    println!("  {}", color_rgb("Custom RGB", 255, 100, 50));
    println!("  {}", bg_color_rgb("Custom RGB BG", 50, 100, 200));

    println!("\nComposed (Style Builder):");
    let s = Style::new().bold().fg("red");
    println!("  {}", s.apply("Bold Red"));

    let s2 = Style::new().italic().fg("blue").bg256(226);
    println!("  {}", s2.apply("Italic Blue on Yellow BG"));

    let s3 = Style::new().bold().underline().fgrgb(255, 100, 50);
    println!("  {}", s3.apply("Bold Underline Custom RGB"));

    println!("\nStrip ANSI:");
    let colored = format!("{} {}", red("Hello"), bold("World"));
    println!("  Original: {}", colored);
    println!("  Stripped: {}", strip_ansi(&colored));

    println!("\n=== End Demo ===");
}