from pwn import *

shell = ssh('bandit9', 'bandit.labs.overthewire.org', password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR', port=2220)


flag = shell["strings data.txt | grep \"^==\" | tail -n 1 | cut -d' ' -f2"]

print flag

# shell.interactive()

