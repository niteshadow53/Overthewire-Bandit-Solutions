from pwn import *

s = ssh('bandit14', 'bandit.labs.overthewire.org', password='4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e', port=2220)


context.log_level = 'debug'
shell = s.shell('/bin/bash')
shell.sendline('telnet localhost 30000')
shell.sendline('4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e')
shell.recvline(timeout=4)
# shell.interactive()

