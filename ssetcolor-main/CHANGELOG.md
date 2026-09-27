# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0]

### Added
- Node.js bindings (`node/`) — pure-JS module, test suite (`node/test.js`), and demo (`node/demo.js`).
- Go bindings (`go/`) — module, cgo-style API surface, tests, and `cmd/demo`.
- Rust bindings (`rust/`) — `lib.rs`, tests, and `examples/demo.rs`.
- Lua bindings (`lua/`) — LuaJIT FFI module with a pure-Lua fallback, tests, and demo.
- Optional CMake custom targets for running the Go, Rust, and Lua test/demo programs.
- CI workflow (`.github/workflows/ci.yml`) building and testing C, Go, Rust, Lua, Node, and Python.
- `LICENSE` (MIT) and this `CHANGELOG.md`.

### Changed
- README extended with quick-start examples and project structure for all bindings.

## [2.0.0] - 2026-07-30

### Added
- Core C library as a shared library (`ssetcolor.dll` / `.so` / `.dylib`).
- C++ header-only wrapper (`cpp/ssetcolor.hpp`).
- Python bindings (`python/`) via ctypes with a pure-Python fallback.
- C API surface: styles, colors, 256-color, truecolor, style builder, and utilities.
- C and Python test suites, plus C and C++ demos.
