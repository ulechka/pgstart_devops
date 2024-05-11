The script installs PostgreSQL on the remote host.
The programm is written on python.

The script uses ssh connection,
it installs PostgreSQL on the remote host,
and configure it to receive connections.

So, the script consists of the following parts:
1) it should take parameters for the connection to the remote host: login, ip (use public key to connect)
# in the task definition there is no login in parameters, so the login would be predefined if empty
# predefined login is admin (web hosters default) or root (linux/unix default to administrate os)
# I think, optimal solution is admin with sudo if it is needed to install postgresql (TODO: look for this info in PS docs)

2) it should know what kind of OS is on the remote host
# I can make an assumption here, that it is macos, because I have macos to work on
# also, check the differencies of implementations for macos and linux on the python described in the py documentation
# also, check the differencies of implementations in the PS docs

3) it connects via ssh to the remote host
# it may need password, but I think it is not secure, so I omit this option
# this program works only with public key on the remote host

4) it installs PostgreSQL
# it needs some installer or source to install
# it should be downloaded from internet
# * maybe it is downloaded on the remote host (if the host is connected to the internet for outgoing connections),
# * and maybe it's downloaded local, and then it is copied to the remote host via ssh/scp
# TODO: look for installation instruction
# so here: remote download - install or local download - remote copy - install

# check if it has installed PS


5) configure PostgreSQL to receive remote requests
# TODO: read documentation
# test the result with request "SELECT 1" from local host

Tasks:
1) parse params
- use https://docs.python.org/3/library/argparse.html
- params are: remote_host, remote_login

2) take system info
- use sysinfo = uname bash utility
- check if "Darwin" in sysinfo.stdout to ensure that that is macos

3) connects via ssh to the remote host
- use https://www.fabfile.org/
- info from #1

4) install PostgreSQL
- use documentation https://postgresql.org/docs
- check if it is installed: run command "createdb sjsijsjsiuhuhuyagsgtvditdstvdkusy". Appropriate answer is "command not found"
- write test bash code to install on macos, check if you don't have permission to install
- write python code to install on macos and check for errors and exceptions ()

if it is fresh install, test installation: 
- createdb mydb OR /usr/local/pgsql/bin/createdb mydb
- dropdb mydb
- init db and check config file: "A default pg_hba.conf file is installed when the data directory is initialized by initdb. It is possible to place the authentication configuration file elsewhere, however; see the hba_file configuration parameter."

- save PGHOST and PGPORT info in the file, provide it to the site admin
set Path:
PATH=/usr/local/pgsql/bin:$PATH
export PATH
set manPath:
MANPATH=/usr/local/pgsql/share/man:$MANPATH
export MANPATH

5) configure db to receive remote connections
- use documentation 
- check if there is 'admin' db user, if it isn't create one:
CREATE ROLE admin WITH LOGIN PASSWORD '<here some password>'
- check postgresql.conf, what I think I need to change

6) update README and write how to use, 
* requirements: key, permissions, os, dependencies
* usage is written by the program, but should be placed in readme too
* what to get and what to use after: envvar, db user name and pass, ...
