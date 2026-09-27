cmake_minimum_required(VERSION 3.10)
project(ssetcolor VERSION 2.0.0 LANGUAGES C CXX)

# C library (shared only)
add_library(ssetcolor SHARED
    src/ssetcolor.c
)

target_include_directories(ssetcolor
    PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
           $<INSTALL_INTERFACE:include>
)

target_compile_definitions(ssetcolor
    PRIVATE SSETCOLOR_BUILD_SHARED
)

if(WIN32)
    target_link_libraries(ssetcolor PRIVATE kernel32)
endif()

set_target_properties(ssetcolor PROPERTIES
    C_STANDARD 99
    C_STANDARD_REQUIRED ON
    C_EXTENSIONS OFF
    POSITION_INDEPENDENT_CODE ON
    SOVERSION 2
    VERSION 2.0.0
)

# C++ example
add_executable(demo_cpp examples/demo.cpp)
target_link_libraries(demo_cpp PRIVATE ssetcolor)

# C example
add_executable(demo_c examples/demo.c)
target_link_libraries(demo_c PRIVATE ssetcolor)


# C tests
enable_testing()
add_executable(test_c tests/test_c.c)
target_link_libraries(test_c PRIVATE ssetcolor)
target_include_directories(test_c PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
add_test(NAME test_c COMMAND test_c)

# ---------------------------------------------------------------------------
# Optional custom targets for the language bindings (non-blocking).
# These targets are only defined when the corresponding toolchain is on PATH,
# so they never break the base C/C++ build.
# ---------------------------------------------------------------------------

find_program(GO_EXECUTABLE go)
if(GO_EXECUTABLE)
    add_custom_target(demo_go
        COMMAND ${GO_EXECUTABLE} run ./cmd/demo/
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/go
        COMMENT "Run the Go demo"
    )
    add_custom_target(test_go
        COMMAND ${GO_EXECUTABLE} test -v ./...
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/go
        COMMENT "Run the Go tests"
    )
endif()

find_program(CARGO_EXECUTABLE cargo)
if(CARGO_EXECUTABLE)
    add_custom_target(demo_rust
        COMMAND ${CARGO_EXECUTABLE} run --example demo
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/rust
        COMMENT "Run the Rust demo"
    )
    add_custom_target(test_rust
        COMMAND ${CARGO_EXECUTABLE} test
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/rust
        COMMENT "Run the Rust tests"
    )
endif()

find_program(LUAJIT_EXECUTABLE luajit)
if(LUAJIT_EXECUTABLE)
    add_custom_target(demo_lua
        COMMAND ${LUAJIT_EXECUTABLE} demo.lua
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lua
        COMMENT "Run the Lua demo"
    )
    add_custom_target(test_lua
        COMMAND ${LUAJIT_EXECUTABLE} test.lua
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lua
        COMMENT "Run the Lua tests"
    )
endif()

