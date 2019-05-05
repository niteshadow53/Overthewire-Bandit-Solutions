from pwn import *

s = ssh('bandit12', 'bandit.labs.overthewire.org', password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu', port=2220)

def runCommand(cmd):
	sh.sendline(cmd)
	print(sh.recvline(timeout=1))

sh = s.shell('/bin/sh')
sh.sendline("whoami")
sh.sendline("rm /tmp/niteshadow53/*")
sh.sendline("cp data.txt /tmp/niteshadow53")
sh.sendline("cd /tmp/niteshadow53")
sh.sendline("xxd -r data.txt > data.gz")
sh.sendline("gunzip data.gz")
sh.sendline("mv data data.bz")
sh.sendline("bunzip2 data.bz")
sh.sendline("tar -xf data")
sh.sendline("tar -xf data5.bin")
sh.sendline("mv data6.bin data6.bz")
sh.sendline("bunzip2 data6.bz")
sh.sendline("tar -xf data6")
sh.sendline("mv data8.bin data8.gz")
sh.sendline("gunzip data8.gz")
sh.sendline("cat data8 | cut -d ' ' -f4")
for x in range(2):
	print(sh.recvline(timeout=1))
# flag = shell["

# print flag

# shell.interactive()
