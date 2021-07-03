import json
import os
from . import managePasswords, check

DOMAINS = {
    "instagram": [],
    "facebook": [],
    "gmail": [],
    "outlook": [],
    "twitter": [],
}


class User:
    def __init__(self):
        if check.osType() == "win32":
            self.__homePath = check.getEnv("USERPROFILE")
        else:
            self.__homePath = check.getEnv("HOME")

        if check.isPwdSet(self.__homePath, check.MASTER_PASSWORD):
            passwd = input("Hello! Enter you master password: ")
            self.sayHello(passwd)
        else:
            master_password = input(
                "Hello! Never saw you here! Please register yourself with a master password.\nPassword: ")
            self.registerUser(master_password)

    def sayHello(self, passwd):
        # passwd = input("Hello! Enter you master password: ")
        with open(os.path.join(self.__homePath, check.MASTER_PASSWORD), "r") as masterPasswdFile:
            newPasswd = json.loads(masterPasswdFile.read()).get("password")
            if newPasswd == passwd:
                myPasswords = managePasswords.managePassword(self.__homePath)
                _main(myPasswords)

    def registerUser(self, masterPassword):
        # masterPassword = input(
        #     "Hello! Never saw you here! Please register yourself with a master password.\nPassword: ")
        with open(os.path.join(self.__homePath, check.MASTER_PASSWORD), "w") as masterPasswdFile:
            newPasswd = json.dumps(
                {
                    "password": masterPassword
                }
            )
            masterPasswdFile.write(newPasswd)
        with open(os.path.join(self.__homePath, check.OTHER_PASSWORDS), "w") as passwdFile:
            defaultPasswd = json.dumps(DOMAINS)
            passwdFile.write(defaultPasswd)
        self.sayHello()


def _main(myPasswords):
    while True:
        ask = input("\n0. Quit\n1. Add password\n2. Get Password\nEnter your choice: ")
        if ask == "1":
            myPasswords.addPasswords()
        elif ask == "2":
            myPasswords.getPasswords()
        elif ask == "0":
            exit(0)
        else:
            print("""\n------------------------------------
| Invalid option. Try again later. |
------------------------------------""")
            _main(myPasswords)
