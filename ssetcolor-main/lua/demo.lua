-- ssetcolor Lua demo
--
-- Run with:  luajit lua/demo.lua

local dir = (arg and arg[0] and arg[0]:match("^(.*)[/\\]")) or "."
package.path = dir .. "/?.lua;" .. package.path

local ssc = require("ssetcolor")

ssc.demo()
