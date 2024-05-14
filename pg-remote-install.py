import argparse
import subprocess
from installer import Installer

# Parse parameters
# programm has 4 parameters:
# remote_host, ssh_login, db_login, db_user
# remote_host is used to connect via ssh
# ssh_login is used to connect via ssh
# db_login is used to run db server
# db_user is created in the db for site admin or smth like that.

parser = argparse.ArgumentParser("pg-remote-install")
parser.add_argument("remote_host", help="Remote host is a domain name or IP", type=str)
parser.add_argument("ssh_login", nargs='?', help="Remote login is the user on the remote host to install software", type=str, default="admin")
parser.add_argument("db_login", nargs='?', help="Remote login is the user on the remote host to run db server", type=str, default="postgres")
parser.add_argument("db_user", nargs='?', help="Remote login is the user on the remote host to run db server", type=str, default="siteadmin")
args = parser.parse_args()
host = args.remote_host
ssh_login = args.ssh_login
db_login = args.db_login
db_user = args.db_user
print("Run with params: {} {} {} {}".format(host, ssh_login, db_login, db_user))

# maybe need to check remote_host param, maybe it would be checked by ssh connection module
#TODO: test with different mistakes in remote host param
#TODO: test without mistakes

installer = Installer(host, ssh_login, db_login, db_user)
# installer.install()

# run local script to check DB is working

add_pass="echo \"{}:5432:mydb:{}:paroleparole\" >> ~/.pgpass".format(host, db_user)
subprocess.run(add_pass)
chmod="chmod 0600 ~/.pgpass"
subprocess.run(chmod)

select="psql -h {} -p 5432 -U {} -w -d mydb -c \"SELECT 1;\"".format(host, db_user)
subprocess.run(select)

print("you can run the following command on your terminal to chech if db is available:\n {}".format(select))



