# ssetcolor — Multi-Language Binding Plan

> **Date:** 2026-07-30
> **Project:** ssetcolor v2.0 — Simple, Honest Terminal Color Library
> **Repository:** https://github.com/Anen135/ssetcolor.git

---

## Table of Contents

1. [Current State](#1-current-state)
2. [Architecture Overview](#2-architecture-overview)
3. [Language Binding Strategy](#3-language-binding-strategy)
4. [Binding: Rust](#4-binding-rust)
5. [Binding: Go](#5-binding-go)
6. [Binding: Lua](#6-binding-lua)
7. [Build Integration](#7-build-integration)
8. [Documentation Updates](#8-documentation-updates)
9. [Testing Strategy](#9-testing-strategy)
10. [File Manifest](#10-file-manifest)

---

## 1. Current State

### ✅ Supported Languages

| Language | Implementation | Location |
|----------|----------------|----------|
| **C** | Core shared library (`.dll`/`.so`/`.dylib`) | `include/ssetcolor.h`, `src/ssetcolor.c` |
| **C++** | Header-only wrapper | `cpp/ssetcolor.hpp` |
| **Python** | ctypes bindings with pure-Python fallback | `python/ssetcolor/__init__.py` |
| **Rust** | Pure Rust implementation | `rust/src/lib.rs`, `rust/tests/tests.rs`, `rust/examples/demo.rs` |
| **Go** | Pure Go implementation | `go/ssetcolor.go`, `go/ssetcolor_test.go`, `go/cmd/demo/main.go` |
| **Lua** | LuaJIT FFI with pure-Lua fallback | `lua/ssetcolor.lua`, `lua/test.lua`, `lua/demo.lua` |
| **Node.js** | Pure JavaScript implementation | `node/ssetcolor.js`, `node/test.js`, `node/demo.js` |

> **Note:** All bindings expose the same ANSI API. The **Rust, Go, and Node.js**
> bindings are standalone pure implementations; the **Python and Lua** bindings use
> the compiled shared library when available and fall back to pure implementations.
> None of the bindings recompile the C code.

### C API Surface (source of truth: `include/ssetcolor.h`)

All bindings wrap the same C functions exported via `SSC_API`:

| Category | Functions |
|----------|-----------|
| **Capability detection** | `ssc_supports_color()`, `ssc_color_depth()` |
| **Low-level wrap** | `ssc_wrap(text, code)`, `ssc_wrap_buf(buf, size, text, code)` |
| **Style builder** | `ssc_style_new()`, `ssc_style_free()`, `ssc_style_add()`, `ssc_style_add_fg()`, `ssc_style_add_bg()`, `ssc_style_add_fg_256()`, `ssc_style_add_bg_256()`, `ssc_style_add_fg_rgb()`, `ssc_style_add_bg_rgb()`, `ssc_style_apply()`, `ssc_style_apply_buf()` |
| **Style helpers** (9) | `ssc_bold`, `ssc_fade`, `ssc_italic`, `ssc_underline`, `ssc_blink_slow`, `ssc_blink_fast`, `ssc_reverse`, `ssc_hidden`, `ssc_concealed` |
| **FG colors** (8) | `ssc_black` – `ssc_white` |
| **BG colors** (8) | `ssc_bg_black` – `ssc_bg_white` |
| **Bright FG** (8) | `ssc_bright_black` – `ssc_bright_white` |
| **Bright BG** (8) | `ssc_bg_bright_black` – `ssc_bg_bright_white` |
| **256-color** | `ssc_color_256(text, code)`, `ssc_bg_color_256(text, code)` |
| **TrueColor** | `ssc_color_rgb(text, r, g, b)`, `ssc_bg_color_rgb(text, r, g, b)` |
| **Utilities** | `ssc_free(ptr)`, `ssc_demo()`, `ssc_strip_ansi(text)` |

---

## 2. Architecture Overview

```
┌──────────────────────────────────────────────────────┐
│                   User Application                    │
├──────────┬──────────┬──────────┬──────────┬──────────┤
│    C     │   C++    │  Python  │   Rust   │    Go    │  Lua  │
│ (direct) │ (header) │ (ctypes) │ (#[link])│  (cgo)   │ (FFI) │
└────┬─────┴────┬─────┴────┬────┴─────┬────┴─────┬────┘
     │          │          │         │          │
     └──────────┴──────────┴─────────┴──────────┘
                         │
              ┌──────────▼──────────┐
              │  libssetcolor.dll   │
              │  libssetcolor.so    │
              │  libssetcolor.dylib │
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │   C Implementation  │
              │  (src/ssetcolor.c)  │
              └─────────────────────┘
```

The **Python** and **Lua** bindings load the shared library at runtime (ctypes / LuaJIT FFI) when available, falling back to pure implementations. The **Rust, Go, and Node.js** bindings are standalone pure implementations of the same ANSI API. No binding recompiles the C code.
