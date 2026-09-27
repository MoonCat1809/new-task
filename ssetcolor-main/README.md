# ssetcolor v2.1.0 — Simple, Honest Terminal Color Library

A lightweight library for coloring terminal output with ANSI escape codes.
Compiled as a shared library (.dll / .so / .dylib) for C and C++, with official
bindings for **Python, Rust, Go, Lua, and Node.js** — plus any language that can call
C functions.

The **Rust, Go, and Node.js** bindings are standalone pure implementations of the
ANSI API; the **Python** and **Lua** bindings use the compiled shared library when
available and fall back to pure implementations.

## Why ssetcolor?

No dependencies. No configuration files. No bloated templates.
Just functions that wrap text in ANSI codes. **Honest.**

## Quick Start

### C

```c
#include "ssetcolor.h"
#include <stdio.h>

int main() {
    char* text = ssc_bold(ssc_red("Hello, World!"));
    printf("%s\n", text);
    ssc_free(text);
    return 0;
}
```

### C++

```cpp
#include "ssetcolor.hpp"
#include <iostream>

int main() {
    std::cout << ssetcolor::bold(ssetcolor::red("Hello!")) << std::endl;
    // Or use the style builder:
    auto s = ssetcolor::style().bold().fg("red");
    std::cout << s.apply("Styled text") << std::endl;
    return 0;
}
```

### Python

```python
from ssetcolor import red, bold, style

print(bold(red("Hello!")))
# Or use the style builder:
s = style().bold().fg("red")
print(s.apply("Styled text"))
```

### Rust

```rust
use ssetcolor::{bold, red, Style};

fn main() {
    println!("{}", bold(&red("Hello, World!")));
    // Or use the style builder:
    let s = Style::new().bold().fg("red");
    println!("{}", s.apply("Styled text"));
}
```

### Go

```go
package main

import (
    "fmt"

    "github.com/Anen135/ssetcolor/go"
)

func main() {
    fmt.Println(ssetcolor.Bold(ssetcolor.Red("Hello, World!")))
    // Or use the style builder:
    s := ssetcolor.NewStyle()
    s.Bold().FG("red")
    fmt.Println(s.Apply("Styled text"))
}
```

### Lua

```lua
local ssetcolor = require("ssetcolor")

print(ssetcolor.bold(ssetcolor.red("Hello, World!")))
-- Or use the style builder:
local s = ssetcolor.style():bold():fg("red")
print(s:apply("Styled text"))
```

### Node.js

```javascript
const ssc = require("./ssetcolor");

console.log(ssc.bold(ssc.red("Hello, World!")));
// Or use the style builder:
console.log(ssc.style().bold().fg("red").apply("Styled text"));
```

## Building

```bash
mkdir build && cd build
cmake .. -G Ninja
cmake --build .
```

## API Reference

### C API (`ssetcolor.h`)

| Function | Description |
|----------|-------------|
| `ssc_bold(text)` | Bold text |
| `ssc_fade(text)` | Faded/low-intensity text |
| `ssc_italic(text)` | Italic text |
| `ssc_underline(text)` | Underlined text |
| `ssc_blink_slow(text)` | Slow blinking text |
| `ssc_blink_fast(text)` | Fast blinking text |
| `ssc_reverse(text)` | Reverse video text |
| `ssc_hidden(text)` | Hidden text |
| `ssc_concealed(text)` | Concealed text |
| `ssc_black(text)` | Black foreground |
| `ssc_red(text)` | Red foreground |
| `ssc_green(text)` | Green foreground |
| `ssc_yellow(text)` | Yellow foreground |
| `ssc_blue(text)` | Blue foreground |
| `ssc_magenta(text)` | Magenta foreground |
| `ssc_cyan(text)` | Cyan foreground |
| `ssc_white(text)` | White foreground |
| `ssc_bg_red(text)` | Red background |
| `ssc_bright_red(text)` | Bright red foreground |
| `ssc_bg_bright_red(text)` | Bright red background |
| `ssc_color_256(text, code)` | 256-color foreground |
| `ssc_bg_color_256(text, code)` | 256-color background |
| `ssc_color_rgb(text, r, g, b)` | Truecolor foreground |
| `ssc_bg_color_rgb(text, r, g, b)` | Truecolor background |
| `ssc_style_new()` | Create a composable style |
| `ssc_style_add(style, code)` | Add ANSI code to style |
| `ssc_style_add_fg(style, name)` | Add foreground color to style |
| `ssc_style_add_bg(style, name)` | Add background color to style |
| `ssc_style_apply(style, text)` | Apply style to text (returns allocated string) |
| `ssc_strip_ansi(text)` | Remove ANSI codes from string |
| `ssc_supports_color()` | Check if terminal supports color |
| `ssc_demo()` | Print a demo of all styles |
| `ssc_free(ptr)` | Free strings returned by ssc_* functions |

### ANSI Code Constants

The header defines macros for all ANSI escape codes:
- `SSC_RESET`, `SSC_BOLD`, `SSC_ITALIC`, `SSC_UNDERLINE`, etc.
- `SSC_RED`, `SSC_GREEN`, `SSC_BLUE`, ... `SSC_WHITE`
- `SSC_BG_RED`, `SSC_BG_GREEN`, ..., `SSC_BG_WHITE`
- `SSC_BRIGHT_BLACK`, ..., `SSC_BRIGHT_WHITE`
- `SSC_BG_BRIGHT_BLACK`, ..., `SSC_BG_BRIGHT_WHITE`

### Error Handling

All functions that allocate return `NULL` on failure.
Always free returned strings with `ssc_free()`, not `free()`.

### Terminal Detection

- `ssc_supports_color()` — returns 1 if stdout is a color-capable terminal
- `ssc_color_depth()` — returns 0 (none), 16, 256, or 16777216 (truecolor)

## Project Structure

```
ssetcolor/
├── CMakeLists.txt          # Build system
├── include/
│   └── ssetcolor.h         # C API header
├── src/
│   └── ssetcolor.c         # C implementation
├── cpp/
│   └── ssetcolor.hpp       # C++ wrapper (header-only)
├── python/
│   ├── pyproject.toml
│   └── ssetcolor/
│       └── __init__.py     # Python bindings
├── go/
│   ├── go.mod
│   ├── ssetcolor.go          # Go bindings
│   ├── ssetcolor_test.go     # Go tests
│   └── cmd/demo/
│       └── main.go           # Go demo
├── rust/
│   ├── Cargo.toml
│   ├── src/
│   │   └── lib.rs            # Rust bindings
│   ├── tests/
│   │   └── tests.rs          # Rust tests
│   └── examples/
│       └── demo.rs           # Rust demo
├── lua/
│   ├── ssetcolor.lua         # Lua bindings (LuaJIT FFI + pure fallback)
│   ├── test.lua              # Lua tests
│   └── demo.lua              # Lua demo
├── node/
│   ├── package.json
│   ├── ssetcolor.js          # Node.js bindings
│   ├── test.js               # Node.js tests
│   └── demo.js               # Node.js demo
├── docs/
│   └── binding-plan.md       # Multi-language binding plan
├── tests/
│   ├── test_c.c            # C tests
│   └── test_python.py      # Python tests
├── examples/
│   ├── demo.c              # C demo
│   └── demo.cpp            # C++ demo
└── build/                  # Build output
```

## License

MIT
