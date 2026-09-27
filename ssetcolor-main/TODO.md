# ssetcolor — Release Readiness TODO

> **Goal:** Bring ssetcolor v2.1.0 to a clean, releasable state.
> **Scope:** Core C/C++ library plus official bindings for **Python, Rust, Go, Lua, and Node.js**.
> **Repository:** https://github.com/Anen135/ssetcolor.git

---

## Phase 1: Release Packaging

- [x] **1.1** Add `LICENSE` (MIT) file
- [x] **1.2** Add `CHANGELOG.md` summarizing changes per release
- [x] **1.3** Confirm versioning (`README.md` / `CMakeLists.txt`) and prepare release tag

## Phase 2: Documentation Refresh

- [x] **2.1** Update `README.md` to include Node.js
  - [x] Add Node.js to the project description
  - [x] Add a Node.js quick-start example
  - [x] Add Node.js to the project structure tree
- [x] **2.2** Update `docs/binding-plan.md` from "planned" to implemented
  - [x] Mark Rust, Go, Lua, Node as implemented
  - [x] Refresh the current-state and architecture sections
- [x] **2.3** Clarify that the high-level bindings are standalone (pure) implementations

## Phase 3: Automated CI

- [x] **3.1** Add GitHub Actions workflow (`.github/workflows/ci.yml`)
  - [x] Build the C library and run the C tests (CTest)
  - [x] Run Go tests (`go test ./...`)
  - [x] Run Rust tests (`cargo test`)
  - [x] Run Node tests (`node node/test.js`)
  - [x] Run Lua tests with LuaJIT (`luajit lua/test.lua`)
  - [x] Run Python tests

## Phase 4: Verification & Final Review

- [x] **4.1** Run every available test suite locally
- [ ] **4.2** Align `colorDepth` behavior across bindings
- [x] **4.3** Final review: clean working tree, no stray artifacts

---
