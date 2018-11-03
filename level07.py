from pwn import *

shell = ssh('bandit7', 'bandit.labs.overthewire.org', password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs', port=2220)


flag = shell['cat data.txt | grep millionth | cut -f2']

print flag

# shell.interactive()

