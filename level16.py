from pwn import *

s = ssh('bandit16', 'bandit.labs.overthewire.org', password='cluFn7wTiGryunymYOu4RcffSxQluehd', port=2220)


context.log_level = 'debug'
shell = s.shell('/bin/bash')
shell.sendline("openssl s_client -connect localhost:31790")
shell.sendline("cluFn7wTiGryunymYOu4RcffSxQluehd")

print shell.recvline_contains("Correct!")
line = shell.recvline_contains("BEGIN RSA PRIVATE KEY")
lines = []
while "END RSA PRIVATE KEY" not in line:
	lines.append(line)
	line = shell.recvline()
lines.append(line)

file = open('bandit17key.private', 'w')
for l in lines:
	file.write(l.strip() + '\n')
# Now we have to set the permissions on the key file
s_local = process('/bin/bash')
s_local.sendline("chmod 700 bandit17key.private")
s_local.sendline("ssh-keygen -i -e -f bandit17key.private > bandit17key2.pem")
s_local.sendline("chmod 700 bandit17key2.private")
s_local.sendline("chmod 700 bandit17key2.pem")


s = ssh('bandit17', 'bandit.labs.overthewire.org', keyfile='bandit17key.private', port=2220)
shell = s.shell("/bin/bash")
shell.interactive()

# Note: Paramiko may have some sort of bug preventing it from successfully detecting the private key. 
# Just use the key to log into the next level



