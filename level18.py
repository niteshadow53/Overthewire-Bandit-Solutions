from pwn import *

# sh = process('/bin/sh')
# context.log_level = 'debug'
sh = process("./level18expect")
lines = sh.recvlines(5)

print("flag: " + lines[4])
