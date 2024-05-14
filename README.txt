Python script installs PostgreSQL on the remote host.

The script uses ssh connection,
it installs PostgreSQL on the remote macos,
and configure db to receive connections.

Requirements
1) remote host with macos, its IP and username for ssh, there should be keys to access remote host;
2) username should have permission to run brew;
3) macos should have developer tools installed. it could be achived by running xcode-select --install, but it shows UI dialog with the request, that should be accepted;
4) that's python scripts, you need the Fabric library ($: pip install fabric)

Usage:
pyhton pg-remote-install.py IP username
# I use Python 3.9.6


So, the script contains the following parts:
1) it takes parameters for the connection to the remote host: IP and login (use public key to connect)
# in the task definition there is no username parameter, so the username would be postgres if empty
# I think, optimal solution is admin with sudo if it is needed to install postgresql, I don't understand if it's needed to use 2 users to install and run postgres. Mybe it's one user, but the permission will be changed after.

2) it should know what kind of OS is on the remote host
# I can make an assumption here, that it is macos, because I have macos to work on

3) it connects via ssh to the remote host
# it may need password, but I think it is not secure, so I omit this option
# this program works only with public key on the remote host

4) it installs PostgreSQL
# it uses Homebrew
# check if it has installed PS

5) it runs db server

6) configure PostgreSQL to receive remote requests

Tasks:
1) parse params
- use https://docs.python.org/3/library/argparse.html
- params are: remote_host, ssh_login, db_login, db_user
remote_host is used to connect via ssh
ssh_login is used to connect via ssh, ssh_login should be allowed to run sudo -u db_login without password prompt
db_login is used to run db server
db_user is created in the db for site admin or smth like that.

2) take system info
- use uname
- check if "Darwin" in result to ensure that this is macos

3) connects via ssh to the remote host
- use https://www.fabfile.org/
- info from #1

4) install PostgreSQL
- use documentation https://postgresql.org/docs
- check if it is installed: run command "createdb sjsijsjsiuhuhuyagsgtvditdstvdkusy". Appropriate answer is "command not found"
- write test bash code to install on macos, check if you don't have permission to install
- write python code to install on macos and check for errors and exceptions ()

check local script for details


5) configure db to receive remote connections
- use documentation 
- check if there is 'postgres' db user, if it isn't create one:
CREATE ROLE postgres WITH LOGIN PASSWORD 'parole'
- check postgresql.conf, what I think I need to change

6) update README and write how to use, 
* requirements: key, permissions, os, dependencies
* usage is written by the program, but should be placed in readme too
* what to get and what to use after: envvar, db user name and pass, ...
