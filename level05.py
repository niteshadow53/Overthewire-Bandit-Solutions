from pwn import *

shell = ssh('bandit5', 'bandit.labs.overthewire.org', password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh', port=2220)


flag = shell['cat inhere/maybehere07/.file2']

# find -type f -size 1033c

print flag

shell.interactive()
