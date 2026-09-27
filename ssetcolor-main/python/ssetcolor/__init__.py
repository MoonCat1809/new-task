"""
ssetcolor - Terminal color library (Python bindings)

Uses the compiled C shared library when available,
falls back to pure Python implementation.
"""
import sys
import ctypes
from ctypes import c_char_p, c_int, c_void_p, CDLL

# Try to load the C library
_lib = None
_load_error = None

def _load_library():
    global _lib
    if _lib is not None:
        return True
    names = []
    if sys.platform == "win32":
        names = ["ssetcolor.dll", "libssetcolor.dll"]
    elif sys.platform == "darwin":
        names = ["libssetcolor.dylib", "ssetcolor.dylib"]
    else:
        names = ["libssetcolor.so", "ssetcolor.so"]
    for name in names:
        try:
            _lib = CDLL(name)
            return True
        except OSError:
            continue
    return False

def _init_lib():
    global _lib
    if not _load_library():
        return False
    # Set up function signatures
    _lib.ssc_supports_color.restype = c_int
    _lib.ssc_color_depth.restype = c_int
    _lib.ssc_free.argtypes = [c_char_p]
    _lib.ssc_wrap.argtypes = [c_char_p, c_char_p]
    _lib.ssc_wrap.restype = c_char_p
    _lib.ssc_strip_ansi.argtypes = [c_char_p]
    _lib.ssc_strip_ansi.restype = c_char_p
    _lib.ssc_demo.restype = None
    return True

_init_lib()

# ANSI escape constants (always available)
RESET         = "\033[0m"
BOLD          = "\033[1m"
FADE          = "\033[2m"
ITALIC        = "\033[3m"
UNDERLINE     = "\033[4m"
BLINK_SLOW    = "\033[5m"
BLINK_FAST    = "\033[6m"
REVERSE       = "\033[7m"
HIDDEN        = "\033[8m"
CONCEALED     = "\033[9m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"


def _wrap_fast(text, code):
    """Use C library if available, fallback to pure Python."""
    if _lib:
        try:
            t_bytes = text.encode("utf-8") if isinstance(text, str) else text
            c_bytes = code.encode("utf-8") if isinstance(code, str) else code
            result = _lib.ssc_wrap(t_bytes, c_bytes)
            if result:
                return result.decode("utf-8")
        except:
            pass
    return f"{code}{text}{RESET}"


def _wrap(text, code):
    return f"{code}{text}{RESET}"


# === Style functions ===

def bold(text): return _wrap(text, BOLD)
def fade(text): return _wrap(text, FADE)
def italic(text): return _wrap(text, ITALIC)
def underline(text): return _wrap(text, UNDERLINE)
def blink_slow(text): return _wrap(text, BLINK_SLOW)
def blink_fast(text): return _wrap(text, BLINK_FAST)
def reverse(text): return _wrap(text, REVERSE)
def hidden(text): return _wrap(text, HIDDEN)
def concealed(text): return _wrap(text, CONCEALED)

def black(text): return _wrap(text, BLACK)
def red(text): return _wrap(text, RED)
def green(text): return _wrap(text, GREEN)
def yellow(text): return _wrap(text, YELLOW)
def blue(text): return _wrap(text, BLUE)
def magenta(text): return _wrap(text, MAGENTA)
def cyan(text): return _wrap(text, CYAN)
def white(text): return _wrap(text, WHITE)

def bg_black(text): return _wrap(text, BG_BLACK)
def bg_red(text): return _wrap(text, BG_RED)
def bg_green(text): return _wrap(text, BG_GREEN)
def bg_yellow(text): return _wrap(text, BG_YELLOW)
def bg_blue(text): return _wrap(text, BG_BLUE)
def bg_magenta(text): return _wrap(text, BG_MAGENTA)
def bg_cyan(text): return _wrap(text, BG_CYAN)
def bg_white(text): return _wrap(text, BG_WHITE)

def color_256(text, code):
    return _wrap(text, f"\033[38;5;{code}m")

def bg_color_256(text, code):
    return _wrap(text, f"\033[48;5;{code}m")

def color_rgb(text, r, g, b):
    return _wrap(text, f"\033[38;2;{r};{g};{b}m")

def bg_color_rgb(text, r, g, b):
    return _wrap(text, f"\033[48;2;{r};{g};{b}m")


def supports_color():
    """Check if terminal supports color output."""
    if _lib:
        try:
            return bool(_lib.ssc_supports_color())
        except:
            pass
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def strip_ansi(text):
    """Remove ANSI escape codes from text."""
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


class style:
    """Composable style builder."""
    def __init__(self):
        self._codes = []

    def add(self, code):
        self._codes.append(code)
        return self

    def bold(self): return self.add(BOLD)
    def italic(self): return self.add(ITALIC)
    def underline(self): return self.add(UNDERLINE)
    def reverse(self): return self.add(REVERSE)
    def fade(self): return self.add(FADE)
    def blink(self): return self.add(BLINK_SLOW)
    def hidden(self): return self.add(HIDDEN)

    def fg(self, name):
        code = globals().get(name.upper())
        if code:
            self._codes.append(code)
        return self

    def bg(self, name):
        code = globals().get(f"BG_{name.upper()}")
        if code:
            self._codes.append(code)
        return self

    def fg256(self, c):
        self._codes.append(f"\033[38;5;{c}m")
        return self

    def bg256(self, c):
        self._codes.append(f"\033[48;5;{c}m")
        return self

    def fgrgb(self, r, g, b):
        self._codes.append(f"\033[38;2;{r};{g};{b}m")
        return self

    def bgrgb(self, r, g, b):
        self._codes.append(f"\033[48;2;{r};{g};{b}m")
        return self

    def apply(self, text):
        codes = "".join(self._codes)
        return f"{codes}{text}{RESET}"


class _context_style:
    """Context manager for temporary styling."""
    def __init__(self, code):
        self.code = code

    def __enter__(self):
        print(self.code, end="")

    def __exit__(self, *args):
        print(RESET, end="")


def with_bold():
    return _context_style(BOLD)

def with_red():
    return _context_style(RED)

def demo():
    """Print a demo of all styles and colors."""
    if _lib:
        try:
            _lib.ssc_demo()
            return
        except:
            pass
    print("\n=== ssetcolor Python Demo ===\n")
    print(f"Styles:")
    print(f"  {bold('Bold')}")
    print(f"  {italic('Italic')}")
    print(f"  {underline('Underline')}")
    print(f"  {reverse('Reverse')}")
    print(f"\nForeground:")
    print(f"  {red('Red')} {green('Green')} {blue('Blue')}")
    print(f"  {yellow('Yellow')} {cyan('Cyan')} {magenta('Magenta')}")
    print(f"\nBackground:")
    print(f"  {bg_red('Red BG')} {bg_green('Green BG')} {bg_blue('Blue BG')}")
    print(f"\n256-Color:")
    print(f"  {color_256('Orange(208)', 208)} {color_256('Purple(129)', 129)}")
    print(f"\nTrueColor:")
    print(f"  {color_rgb('CustomRGB', 255, 100, 50)}")
    print(f"\nComposed:")
    s = style().bold().fg("red")
    print(f"  {s.apply('Bold Red')}")
    print("\n=== End Demo ===\n")


if __name__ == "__main__":
    demo()
