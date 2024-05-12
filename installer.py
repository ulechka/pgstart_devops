# documentation https://www.postgresql.org/download/linux/redhat/

class Installer:
    def __init__(self, connection):
        self.connection = connection
    
    def install_on_macos(self, version=16):
        # check if ps is installed
        command = "createdb sjsijsjsiuhuhuyagsgtvditdstvdkusy"
        createdb = connection.run(command)
        if not "command not found" in createdb.stdout:
            # there is some ps
            command = "dropdb sjsijsjsiuhuhuyagsgtvditdstvdkusy"
            dropdb = connection.run(command)
            # TODO: check version
            # TODO: update or not update?
            # TODO: maybe it's ok to configure it anyway
            return
        
        install="brew yinstall postgresql@{}".format(version)
        create_user="CREATE ROLE admin WITH LOGIN PASSWORD '7&29e2V8|o4Ji$l22H(x'"
        create_db="createdb --owner admin test_task_table 'table to test db'"
        # fill_table="INSERT "
        for command in [install, create_user, create_db]:
            print(command)
            command_result = connection.run(command)
            msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
            print(msg.format(command_result))
        
    
#TODO: support other systems
# use docs https://www.postgresql.org/download/
    