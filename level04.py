from pwn import *

shell = ssh('bandit4', 'bandit.labs.overthewire.org', password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB', port=2220)


flag = shell['cat inhere/-file07']

# file ./* | grep -v data

print flag

# shell.interactive()
