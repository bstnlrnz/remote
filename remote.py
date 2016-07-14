import pexpect
import sys
import getpass

#Parameter abfragen

print ("Host IP-Address:"),
src =raw_input()
print("User:"),
usr=raw_input()
print("Command:"),
cmd=raw_input()

# SSH Verbindung herstellen
def connect(src, usr, cmd):
    connStr="ssh " + usr + "@" + src
    child=pexpect.spawn(connStr)
    i=child.expect(['~\$', pexpect.EOF, pexpect.TIMEOUT])
    if i==0:
         child.sendline(cmd)
         h=child.expect(['~\$', 'password'])
         if h==0:
            print ("Output:"),child.before
         elif h==1:
            pw = getpass.getpass("Need sudo password, please give me...:")
            child.sendline(pw)
            child.expect('~\$')
            print child.before
    elif i==1:
         print("End of File")
    elif i==2:
         print("Connection timed out....")

# Main
connect(src, usr, cmd)
