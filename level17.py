from pwn import *

s = ssh('bandit17', 'bandit.labs.overthewire.org', password='xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn', port=2220)

# context.log_level = 'debug'
shell = s.shell('/bin/bash')
shell.sendline("diff passwords.new passwords.old\n")
lines = shell.recvlines(4)
print(lines)

flag = lines[1][2:]
print("Flag: " + flag)

# s.interactive()
