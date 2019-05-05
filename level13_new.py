from pwn import *

s = ssh('bandit13', 'bandit.labs.overthewire.org', password='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL', port=2220)

# def runCommand(cmd):
# 	sh.sendline(cmd)
# 	print(sh.recvline(timeout=1))
	
s.download_file('sshkey.private')
s.interactive()

# s.interactive()



