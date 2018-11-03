from pwn import *

shell = ssh('bandit6', 'bandit.labs.overthewire.org', password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7', port=2220)


flag = shell['find / -user bandit7 -size 33c -group bandit6 2>/dev/null | xargs cat']

print flag

