import pexpect
import sys
import getpass

# Funktion: SSH Verbindung herstellen
def connect(src, usr, cmd):
    connStr="ssh " + usr + "@" + src
    child=pexpect.spawn(connStr)
    #Warten auf Shell-Prompt
    i=child.expect(['~\$', pexpect.EOF, pexpect.TIMEOUT])
    if i==0:
         child.sendline(cmd)
         h=child.expect(['~\$', 'password'])
         if h==0:
            print ("#####################Output:#####################"), child.before
         elif h==1:
            pw = getpass.getpass("Need sudo password, please type in...:")
            child.sendline(pw)
            child.expect('~\$')
            print child.before
    elif i==1:
         print("End of File")
    elif i==2:
         sys.exit("Connection timed out....")

# Main

# Parameter abfragen
if len(sys.argv) < 2:
    print ("Host IP-Address:"),
    src =raw_input()
    print("User:"),
    usr=raw_input()
    print("Command:"),
    cmd=raw_input()
elif len(sys.argv) == 4:
    try:
        src=sys.argv[1]
        usr=sys.argv[2]
        cmd=sys.argv[3]
    except:
        sys.exit("Error - Usage: <IP> <UserName> <\"Command\">")
else:
    sys.exit("Error - Usage: <IP> <UserName> <\"Command\">")

# Funktion aufrufen
connect(src, usr, cmd)
