from os import system
from time import sleep


# update.sh body
app_body = """#!/bin/bash
sudo apt-get update && apt-get upgrade -y"""


def bash_command(user_in):
    _ = system(user_in)


def clear_screen():
    bash_command('clear')


def install_app():
    # Creates the file and gives it executable permission
    bash_command(f"echo '{app_body}' >> update.sh")
    bash_command("chmod +x update.sh")

    # Renames the file for ease-of-typing
    bash_command("mv update.sh update")

    # Makes file executable from any location within Terminal
    bash_command("sudo mv update /usr/bin/update")


def remove_installer():
    response = input("Delete the installer file (y/yes or n/no)?").lower()

    if response == 'y' or response == 'yes':
        # Deletes the installer file
        print("This app will self-destruct.")
        bash_command("sudo rm installer.py")

    elif response == 'n' or response == 'no':
        print("Have a nice day!")
    else:
        print(f""""{response}" is neither "y", nor "yes", nor "n", nor "no".  Please try again.""")
        remove_installer()


if __name__ == '__main__':
    clear_screen()
    print('Installing your app...\n')
    install_app()

    print('Your app is installed!')
    sleep(1.25)

    clear_screen()
    remove_installer()
