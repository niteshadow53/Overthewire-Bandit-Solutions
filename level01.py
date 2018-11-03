from pwn import *

shell = ssh('bandit1', 'bandit.labs.overthewire.org', password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1', port=2220)

flag = shell['cat ./-']

print("flag: " + flag)

# shell.interactive()
