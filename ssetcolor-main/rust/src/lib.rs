//! ssetcolor — Terminal color library for Rust
//!
//! Pure Rust implementation of ANSI escape code generation for terminal colors.
//! No external dependencies required.

/// ANSI escape code constants
pub mod ansi {
    pub const RESET: &str = "\x1b[0m";
    pub const BOLD: &str = "\x1b[1m";
    pub const FADE: &str = "\x1b[2m";
    pub const ITALIC: &str = "\x1b[3m";
    pub const UNDERLINE: &str = "\x1b[4m";
    pub const BLINK_SLOW: &str = "\x1b[5m";
    pub const BLINK_FAST: &str = "\x1b[6m";
    pub const REVERSE: &str = "\x1b[7m";
    pub const HIDDEN: &str = "\x1b[8m";
    pub const CONCEALED: &str = "\x1b[9m";
    pub const BOLD_OFF: &str = "\x1b[21m";
    pub const ITALIC_OFF: &str = "\x1b[23m";
    pub const UNDERLINE_OFF: &str = "\x1b[24m";
    pub const BLINK_OFF: &str = "\x1b[25m";
    pub const REVERSE_OFF: &str = "\x1b[27m";
    pub const HIDDEN_OFF: &str = "\x1b[28m";

    pub const BLACK: &str = "\x1b[30m";
    pub const RED: &str = "\x1b[31m";
    pub const GREEN: &str = "\x1b[32m";
    pub const YELLOW: &str = "\x1b[33m";
    pub const BLUE: &str = "\x1b[34m";
    pub const MAGENTA: &str = "\x1b[35m";
    pub const CYAN: &str = "\x1b[36m";
    pub const WHITE: &str = "\x1b[37m";

    pub const BRIGHT_BLACK: &str = "\x1b[90m";
    pub const BRIGHT_RED: &str = "\x1b[91m";
    pub const BRIGHT_GREEN: &str = "\x1b[92m";
    pub const BRIGHT_YELLOW: &str = "\x1b[93m";
    pub const BRIGHT_BLUE: &str = "\x1b[94m";
    pub const BRIGHT_MAGENTA: &str = "\x1b[95m";
    pub const BRIGHT_CYAN: &str = "\x1b[96m";
    pub const BRIGHT_WHITE: &str = "\x1b[97m";

    pub const BG_BLACK: &str = "\x1b[40m";
    pub const BG_RED: &str = "\x1b[41m";
    pub const BG_GREEN: &str = "\x1b[42m";
    pub const BG_YELLOW: &str = "\x1b[43m";
    pub const BG_BLUE: &str = "\x1b[44m";
    pub const BG_MAGENTA: &str = "\x1b[45m";
    pub const BG_CYAN: &str = "\x1b[46m";
    pub const BG_WHITE: &str = "\x1b[47m";

    pub const BG_BRIGHT_BLACK: &str = "\x1b[100m";
    pub const BG_BRIGHT_RED: &str = "\x1b[101m";
    pub const BG_BRIGHT_GREEN: &str = "\x1b[102m";
    pub const BG_BRIGHT_YELLOW: &str = "\x1b[103m";
    pub const BG_BRIGHT_BLUE: &str = "\x1b[104m";
    pub const BG_BRIGHT_MAGENTA: &str = "\x1b[105m";
    pub const BG_BRIGHT_CYAN: &str = "\x1b[106m";
    pub const BG_BRIGHT_WHITE: &str = "\x1b[107m";
}

/// Wraps text with an ANSI code and reset.
fn wrap(text: &str, code: &str) -> String {
    format!("{}{}{}", code, text, ansi::RESET)
}

/// Check if the terminal supports color output.
pub fn supports_color() -> bool {
    true
}

/// Returns the terminal color depth (0 = none, 4 = basic, 8 = 256, 24 = truecolor).
pub fn color_depth() -> u8 {
    24
}

// === Style functions ===

pub fn bold(text: &str) -> String { wrap(text, ansi::BOLD) }
pub fn fade(text: &str) -> String { wrap(text, ansi::FADE) }
pub fn italic(text: &str) -> String { wrap(text, ansi::ITALIC) }
pub fn underline(text: &str) -> String { wrap(text, ansi::UNDERLINE) }
pub fn blink_slow(text: &str) -> String { wrap(text, ansi::BLINK_SLOW) }
pub fn blink_fast(text: &str) -> String { wrap(text, ansi::BLINK_FAST) }
pub fn reverse(text: &str) -> String { wrap(text, ansi::REVERSE) }
pub fn hidden(text: &str) -> String { wrap(text, ansi::HIDDEN) }
pub fn concealed(text: &str) -> String { wrap(text, ansi::CONCEALED) }

// === Foreground color functions ===

pub fn black(text: &str) -> String { wrap(text, ansi::BLACK) }
pub fn red(text: &str) -> String { wrap(text, ansi::RED) }
pub fn green(text: &str) -> String { wrap(text, ansi::GREEN) }
pub fn yellow(text: &str) -> String { wrap(text, ansi::YELLOW) }
pub fn blue(text: &str) -> String { wrap(text, ansi::BLUE) }
pub fn magenta(text: &str) -> String { wrap(text, ansi::MAGENTA) }
pub fn cyan(text: &str) -> String { wrap(text, ansi::CYAN) }
pub fn white(text: &str) -> String { wrap(text, ansi::WHITE) }

// === Background color functions ===

pub fn bg_black(text: &str) -> String { wrap(text, ansi::BG_BLACK) }
pub fn bg_red(text: &str) -> String { wrap(text, ansi::BG_RED) }
pub fn bg_green(text: &str) -> String { wrap(text, ansi::BG_GREEN) }
pub fn bg_yellow(text: &str) -> String { wrap(text, ansi::BG_YELLOW) }
pub fn bg_blue(text: &str) -> String { wrap(text, ansi::BG_BLUE) }
pub fn bg_magenta(text: &str) -> String { wrap(text, ansi::BG_MAGENTA) }
pub fn bg_cyan(text: &str) -> String { wrap(text, ansi::BG_CYAN) }
pub fn bg_white(text: &str) -> String { wrap(text, ansi::BG_WHITE) }

// === Bright foreground color functions ===

pub fn bright_black(text: &str) -> String { wrap(text, ansi::BRIGHT_BLACK) }
pub fn bright_red(text: &str) -> String { wrap(text, ansi::BRIGHT_RED) }
pub fn bright_green(text: &str) -> String { wrap(text, ansi::BRIGHT_GREEN) }
pub fn bright_yellow(text: &str) -> String { wrap(text, ansi::BRIGHT_YELLOW) }
pub fn bright_blue(text: &str) -> String { wrap(text, ansi::BRIGHT_BLUE) }
pub fn bright_magenta(text: &str) -> String { wrap(text, ansi::BRIGHT_MAGENTA) }
pub fn bright_cyan(text: &str) -> String { wrap(text, ansi::BRIGHT_CYAN) }
pub fn bright_white(text: &str) -> String { wrap(text, ansi::BRIGHT_WHITE) }

// === Bright background color functions ===

pub fn bg_bright_black(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_BLACK) }
pub fn bg_bright_red(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_RED) }
pub fn bg_bright_green(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_GREEN) }
pub fn bg_bright_yellow(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_YELLOW) }
pub fn bg_bright_blue(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_BLUE) }
pub fn bg_bright_magenta(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_MAGENTA) }
pub fn bg_bright_cyan(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_CYAN) }
pub fn bg_bright_white(text: &str) -> String { wrap(text, ansi::BG_BRIGHT_WHITE) }

// === 256-color functions ===

pub fn color_256(text: &str, color_code: u8) -> String {
    wrap(text, &format!("\x1b[38;5;{}m", color_code))
}

pub fn bg_color_256(text: &str, color_code: u8) -> String {
    wrap(text, &format!("\x1b[48;5;{}m", color_code))
}

// === TrueColor functions ===

pub fn color_rgb(text: &str, r: u8, g: u8, b: u8) -> String {
    wrap(text, &format!("\x1b[38;2;{};{};{}m", r, g, b))
}

pub fn bg_color_rgb(text: &str, r: u8, g: u8, b: u8) -> String {
    wrap(text, &format!("\x1b[48;2;{};{};{}m", r, g, b))
}

// === Utility functions ===

/// Removes ANSI escape codes from the given text.
pub fn strip_ansi(text: &str) -> String {
    let mut result = String::with_capacity(text.len());
    let mut chars = text.chars().peekable();
    while let Some(c) = chars.next() {
        if c == '\x1b' && chars.peek() == Some(&'[') {
            chars.next(); // consume '['
            while let Some(&next) = chars.peek() {
                if next == 'm' {
                    chars.next(); // consume 'm'
                    break;
                }
                chars.next();
            }
        } else {
            result.push(c);
        }
    }
    result
}

/// Prints a demonstration of all styles and colors.
pub fn demo() {
    println!("\n=== ssetcolor Rust Demo ===\n");

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

/// Composable style builder.
#[derive(Default, Clone)]
pub struct Style {
    codes: Vec<String>,
}

impl Style {
    /// Creates a new Style builder.
    pub fn new() -> Self {
        Style { codes: Vec::new() }
    }

    /// Adds a raw ANSI code to the style.
    pub fn add(mut self, code: &str) -> Self {
        self.codes.push(code.to_string());
        self
    }

    /// Adds bold style.
    pub fn bold(self) -> Self { self.add(ansi::BOLD) }

    /// Adds italic style.
    pub fn italic(self) -> Self { self.add(ansi::ITALIC) }

    /// Adds underline style.
    pub fn underline(self) -> Self { self.add(ansi::UNDERLINE) }

    /// Adds fade (dim) style.
    pub fn fade(self) -> Self { self.add(ansi::FADE) }

    /// Adds reverse video style.
    pub fn reverse(self) -> Self { self.add(ansi::REVERSE) }

    /// Adds slow blink style.
    pub fn blink(self) -> Self { self.add(ansi::BLINK_SLOW) }

    /// Adds hidden (concealed) style.
    pub fn hidden(self) -> Self { self.add(ansi::HIDDEN) }

    /// Sets the foreground color by name (e.g., "red", "green").
    pub fn fg(self, color_name: &str) -> Self {
        if let Some(code) = fg_color_map(color_name) {
            self.add(code)
        } else {
            self
        }
    }

    /// Sets the background color by name (e.g., "red", "green").
    pub fn bg(self, color_name: &str) -> Self {
        if let Some(code) = bg_color_map(color_name) {
            self.add(code)
        } else {
            self
        }
    }

    /// Sets the foreground to a 256-color code.
    pub fn fg256(self, color_code: u8) -> Self {
        self.add(&format!("\x1b[38;5;{}m", color_code))
    }

    /// Sets the background to a 256-color code.
    pub fn bg256(self, color_code: u8) -> Self {
        self.add(&format!("\x1b[48;5;{}m", color_code))
    }

    /// Sets the foreground to a truecolor RGB value.
    pub fn fgrgb(self, r: u8, g: u8, b: u8) -> Self {
        self.add(&format!("\x1b[38;2;{};{};{}m", r, g, b))
    }

    /// Sets the background to a truecolor RGB value.
    pub fn bgrgb(self, r: u8, g: u8, b: u8) -> Self {
        self.add(&format!("\x1b[48;2;{};{};{}m", r, g, b))
    }

    /// Applies the style to the given text and returns the wrapped result.
    pub fn apply(&self, text: &str) -> String {
        let codes: String = self.codes.join("");
        format!("{}{}{}", codes, text, ansi::RESET)
    }
}

fn fg_color_map(name: &str) -> Option<&'static str> {
    match name.to_lowercase().as_str() {
        "black" => Some(ansi::BLACK),
        "red" => Some(ansi::RED),
        "green" => Some(ansi::GREEN),
        "yellow" => Some(ansi::YELLOW),
        "blue" => Some(ansi::BLUE),
        "magenta" => Some(ansi::MAGENTA),
        "cyan" => Some(ansi::CYAN),
        "white" => Some(ansi::WHITE),
        "bright_black" => Some(ansi::BRIGHT_BLACK),
        "bright_red" => Some(ansi::BRIGHT_RED),
        "bright_green" => Some(ansi::BRIGHT_GREEN),
        "bright_yellow" => Some(ansi::BRIGHT_YELLOW),
        "bright_blue" => Some(ansi::BRIGHT_BLUE),
        "bright_magenta" => Some(ansi::BRIGHT_MAGENTA),
        "bright_cyan" => Some(ansi::BRIGHT_CYAN),
        "bright_white" => Some(ansi::BRIGHT_WHITE),
        _ => None,
    }
}

fn bg_color_map(name: &str) -> Option<&'static str> {
    match name.to_lowercase().as_str() {
        "black" => Some(ansi::BG_BLACK),
        "red" => Some(ansi::BG_RED),
        "green" => Some(ansi::BG_GREEN),
        "yellow" => Some(ansi::BG_YELLOW),
        "blue" => Some(ansi::BG_BLUE),
        "magenta" => Some(ansi::BG_MAGENTA),
        "cyan" => Some(ansi::BG_CYAN),
        "white" => Some(ansi::BG_WHITE),
        "bright_black" => Some(ansi::BG_BRIGHT_BLACK),
        "bright_red" => Some(ansi::BG_BRIGHT_RED),
        "bright_green" => Some(ansi::BG_BRIGHT_GREEN),
        "bright_yellow" => Some(ansi::BG_BRIGHT_YELLOW),
        "bright_blue" => Some(ansi::BG_BRIGHT_BLUE),
        "bright_magenta" => Some(ansi::BG_BRIGHT_MAGENTA),
        "bright_cyan" => Some(ansi::BG_BRIGHT_CYAN),
        "bright_white" => Some(ansi::BG_BRIGHT_WHITE),
        _ => None,
    }
}