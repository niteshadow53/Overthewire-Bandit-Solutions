from pwn import *

shell = ssh('bandit2', 'bandit.labs.overthewire.org', password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9', port=2220)

flag = shell['cat spaces\ in\ this\ filename']

print flag
