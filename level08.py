from pwn import *

shell = ssh('bandit8', 'bandit.labs.overthewire.org', password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV', port=2220)


flag = shell["sort data.txt | uniq -c | grep '1 ' | tr -s ' ' | cut -d ' ' -f3"]

print flag

# shell.interactive()

