import argparse
from fabric import Connection
from installer import Installer

# 1 get params
# programm has 1 required param: IP or domain
# if the number of params less than 1 write usage
# usage: python pg-remote-install.py server.domain.name.or.ip [login]
# if the first param is not the address write usage and error message and exit
# if there is the second parameter on input it should be login
# if there is no second param use admin as default login
# if there is more than 2 params write usage and exit

parser = argparse.ArgumentParser("pg-remote-install")
parser.add_argument("remote_host", help="Remote host is a domain name or IP", type=str)
parser.add_argument("remote_login", nargs='?', help="Remote login is a user name on the remote host", type=str, default="admin")
args = parser.parse_args()
host = args.remote_host
login = args.remote_login
print(host)
print(login)

# maybe need to check remote_host param, maybe it would be checked by ssh connection module
#TODO: test with different mistakes in remote host param
#TODO: test without mistakes

# 2 assumme some state of remote host system
os_needed = "Darwin"

# 3 connect via ssh
# check credentials
# if there is a problem print error message and exit
command = 'uname -s'
c = Connection(host, login)
uname = c.run('uname -s', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(uname))

if os_needed in uname.stdout:
    command = "ls"
    result = c.run(command, hide=True).stdout.strip()
    print(result)




# 4 install PostgreSQL
# check if some version of ps has been istalled
# TODO: check if some version of ps has been istalled
# if the version is the last? do nothing
# if the version is previous write exception message
# if the version could be updated -- update
# if there is noo version install new version

i = Installer()
i.install_on_macos(16)


# 5 configure PostgreSQL to receive remote requests



