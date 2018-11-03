from pwn import *

shell = ssh('bandit10', 'bandit.labs.overthewire.org', password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk', port=2220)


flag = shell["base64 -d data.txt | cut -d ' ' -f4"]

print flag

# shell.interactive()

