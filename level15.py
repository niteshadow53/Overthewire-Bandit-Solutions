from pwn import *
import time

s = ssh('bandit15', 'bandit.labs.overthewire.org', password='BfMYroe26WYalil77FoDi9qh59eK5xNr', port=2220)


# context.log_level = 'debug'
shell = s.shell('/bin/bash')
shell.sendline("openssl s_client -connect localhost:30001")
shell.sendline("BfMYroe26WYalil77FoDi9qh59eK5xNr")

print shell.recvline_contains("Correct!")
print shell.recvline()
# for i in range(70):
# 	print shell.recvline()

