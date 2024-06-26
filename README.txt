Python script installs PostgreSQL on the remote host.

The script uses ssh connection,
it installs PostgreSQL on the remote macos,
and configure db to receive connections.

Requirements
1) remote host with macos, its IP and username for ssh, there should be keys to access remote host;
2) username should have permission to run brew;
3) macos should have developer tools installed. It could be achived by running `xcode-select --install`. Note: it shows UI dialog with the request, that should be accepted;
4) that's python script, using Python 3.9.6 and the Fabric library (~: pip install fabric)

Usage:
python pg-remote-install [-h] remote_host [ssh_login] [db_login] [db_user]
remote_host is used to connect via ssh
ssh_login is used to connect via ssh, ssh_login should be allowed to run sudo -u db_login without password prompt
db_login is used to run db server
db_user is created in the db for site admin or smth like that.



So, the script contains the following parts:
1) it takes parameters for the connection to the remote host: IP and login (use public key to connect)
# in the task definition there is no ssh_login parameter, so the ssh_login would be admin if empty
# in the task definition there is no db_login parameter, so the db_login would be postgres if empty
# in the task definition there is no db_user parameter, so the db_user would be siteadmin if empty

2) it should know what kind of OS is on the remote host
# I can make an assumption here, that it is macos, because I have macos to work on
# TODO: support other systems 

3) it connects via ssh to the remote host
# it may need password, but I think it is not secure, so I omit this option
# this program works only with public key on the remote host

4) it installs PostgreSQL using Homebrew

5) it runs Postgres DB server under db_user

6) edit config files to enable receiving remote requests

7) creates db_user with no Super-User permissions, but with password. Pasword is saved in the local file ~/.pgpass for psql client.


The following text is my plan I worked by
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
