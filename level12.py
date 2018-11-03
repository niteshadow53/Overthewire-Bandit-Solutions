from pwn import *

shell = ssh('bandit12', 'bandit.labs.overthewire.org', password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu', port=2220)

def runCommand(cmd):
	print shell[cmd]

runCommand("mv data.txt /tmp/niteshadow53")
runCommand("cat data.txt")

# flag = shell["

# print flag

shell.interactive()

