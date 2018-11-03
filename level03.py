from pwn import *

shell = ssh('bandit3', 'bandit.labs.overthewire.org', password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK', port=2220)

flag = shell['cat inhere/.hidden']

print flag

shell.interactive()
