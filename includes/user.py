import json
import os
from . import manager, utils

DOMAINS = {
    "instagram": [],
    "facebook": [],
    "gmail": [],
    "outlook": [],
    "twitter": [],
}


class User:
    def __init__(self):
        if utils.os_type() == "win32":
            self.__homePath = utils.get_env("USERPROFILE")
        else:
            self.__homePath = utils.get_env("HOME")

        if utils.is_pwd_set(self.__homePath, utils.MASTER_PASSWORD):
            passwd = input("Hello! Enter you master password: ")
            self.login_user(passwd)
        else:
            master_password = input(
                "Hello! Never saw you here! Please register yourself with a master password.\nPassword: "
            )
            self.register_user(master_password)

    def login_user(self, passwd):
        # passwd = input("Hello! Enter you master password: ")
        with open(
            os.path.join(self.__homePath, utils.MASTER_PASSWORD), "r"
        ) as masterPasswdFile:
            new_passwd = json.loads(masterPasswdFile.read()).get("password")
            if new_passwd == passwd:
                my_passwords = manager.ManagePassword(self.__homePath)
                _main(my_passwords)

    def register_user(self, master_password):
        # masterPassword = input(
        #     "Hello! Never saw you here! Please register yourself with a master password.\nPassword: ")
        with open(
            os.path.join(self.__homePath, utils.MASTER_PASSWORD), "w"
        ) as masterPasswdFile:
            new_passwd = json.dumps({"password": master_password})
            masterPasswdFile.write(new_passwd)
        with open(
            os.path.join(self.__homePath, utils.OTHER_PASSWORDS), "w"
        ) as passwdFile:
            default_passwd = json.dumps(DOMAINS)
            passwdFile.write(default_passwd)
        self.login_user()


def _main(my_passwords):
    while True:
        ask = input("\n0. Quit\n1. Add password\n2. Get Password\n3. List Usernames\nEnter your choice: ")
        if ask == "1":
            my_passwords.add_passwords()
        elif ask == "2":
            my_passwords.get_passwords()
        elif ask == "3":
            my_passwords.list_usernames()
        elif ask == "0":
            exit(0)
        else:
            print(
                """\n------------------------------------
| Invalid option. Try again later. |
------------------------------------"""
            )
            _main(my_passwords)
