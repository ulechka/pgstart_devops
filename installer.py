# documentation https://www.postgresql.org/download/macos/
import invoke
from fabric import Connection


class Installer:
    def __init__(self, host, ssh_login, db_login, db_user):
        self.host = host
        self.ssh_login = ssh_login
        self.db_login = db_login
        self.db_user = db_user
        self.connection = Connection(host, ssh_login)
    
    def is_remote_system_macos(self):
        os_needed = "Darwin"
        uname = self.connection.run('uname -s', hide=True)
        msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
        print(msg.format(uname))
        if os_needed in uname.stdout:
            return True
        return False
    
    def install(self):
        macos = self.is_remote_system_macos()
        if macos:
            self.install_on_macos()
        else:
            print("Sorry, give me another system to make a new script!")
        
    def install_on_macos(self, version=16):
        # check if ps is installed
        installed = True
        command = "createdb sjsijsjsiuhuhuyagsgtvditdstvdkusy"
        try:
            createdb = self.connection.run(command)
            command = "dropdb sjsijsjsiuhuhuyagsgtvditdstvdkusy"
            dropdb = self.connection.run(command)
            # TODO: check version
            # TODO: update or not update?: first version NOT
            # TODO: maybe it's ok to configure it anyway
        except invoke.exceptions.UnexpectedExit as exc:
            # 'command not found' error code = 127
            if exc.result.exited == 127:
                installed = False
        
        if not installed:
            # system paths
            bin_path="/usr/local/opt/postgresql@{}/bin/".format(version)
            data_path="/Users/{}/Documents/pgsql/data/".format(self.db_login)
            
            # commands
            install="/usr/local/bin/brew install postgresql@{}".format(version)
            su_wrapper="su postgres -c '{}'"
            initdb="{0}initdb --locale=C -E UTF-8 /Users/{1}/Documents/pgsql/data".format(bin_path, self.ssh_login)
            start="{}pg_ctl -D /Users/{}/Documents/pgsql/data -l logfile start".format(bin_path, self.ssh_login)
            cd="cd {}".format(data_path)
            # 5 configure PostgreSQL to receive remote requests
            conf_server="sed \"s/#listen_addresses = \'localhost\'/listen_addresses = \'*\'/g\" postgresql.conf >new_conf"
            replace_conf="mv new_conf postgresql.conf"
            conf_hba="echo \"host    mydb            {}        0.0.0.0/0               md5\" >> pg_hba.conf".format(self.db_user)
            createdb="{}createdb mydb".format(bin_path)
            create_dbuser="{}psql -p 5432 -U {} -d mydb -c \"CREATE ROLE {} WITH LOGIN PASSWORD 'paroleparole';\"".format(bin_path, self.db_login, self.db_user)
            # 
            restart="{}pg_ctl restart -D {}".format(bin_path, self.db_login, data_path)
            autorun="/usr/local/bin/brew services start postgresql@16"
            
            list_of_commmands = [
                install,
                su_wrapper.format(initdb),
                su_wrapper.format(start),
                cd, conf_server, replace_conf, conf_hba,
                createdb,
                create_dbuser,
                restart,
                autorun
            ]
            
            
            for command in list_of_commmands:
                print("Run: {}".format(command))
                try:
                    command_result = self.connection.run(command)
                    msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}, stderr:\n{0.stderr}"
                    print(msg.format(command_result))
                except invoke.exceptions.UnexpectedExit as exc:
                    msg = "Error result on command '{}', exit code: {}, errror: {}"
                    print(msg.format(command, exc.result.exited, exc.result.stderr))
        
        
    
#TODO: support other systems
# use docs https://www.postgresql.org/download/
    