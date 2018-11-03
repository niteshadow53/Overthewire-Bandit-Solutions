from pwn import *

s = ssh('bandit13', 'bandit.labs.overthewire.org', password='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL', port=2220)

# def runCommand(cmd):
# 	sh.sendline(cmd)
# 	print(sh.recvline(timeout=1))
	
s.download_file('sshkey.private')

s = ssh('bandit14', 'bandit.labs.overthewire.org', keyfile='sshkey.private', port=2220)

local_s = process("/bin/bash")
local_s.sendline("rm sshkey.private")

shell = s.shell("/bin/bash")
shell.sendline("cat /etc/bandit_pass/bandit14")
print(shell.recvline(timeout=1))

# s.interactive()



