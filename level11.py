from pwn import *

shell = ssh('bandit11', 'bandit.labs.overthewire.org', password='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR', port=2220)


flag = shell["cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'"]

print flag

# shell.interactive()

