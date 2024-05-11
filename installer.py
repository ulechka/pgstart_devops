# documentation https://www.postgresql.org/download/linux/redhat/

class Installer:
    def install_on_macos(version=16, dry_run=True):
        command="brew install postgresql@{}".format(version)
        print(command)
        if not dry_run:
            run_command(command)
            print("the command has been run")
        
    
#TODO: do after check macos version if it's needed
    def install_on_debian(dry_run=True):
        command="apt install postgresql"
        print(command)
        if not dry_run:
            run_command(command)
        # TODO: check on some debian machine
        # sudo apt install -y postgresql-common
        # sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
    