import json
import os

from pmUtils import check, managePasswords

MASTER_PASSWORD = ".masterpwd.json"
OTHER_PASSWORDS = ".password_manager.json"
DOMAINS = {
    "instagram": [],
    "facebook": [],
    "gmail": [],
    "outlook": [],
    "twitter": [],
}


class init:
    def __init__(self):
        checkNewUser()


class checkNewUser:
    def __init__(self):
        if check.osType() == "win32":
            self.__homePath = check.getEnv("USERPROFILE")
        else:
            self.__homePath = check.getEnv("HOME")

        if check.isPwdSet(self.__homePath, MASTER_PASSWORD):
            self.sayHello()
        else:
            self.registerUser()

    def sayHello(self):
        passwd = input("Hello! Enter you master password: ")
        with open(os.path.join(self.__homePath, MASTER_PASSWORD), "r") as masterPasswdFile:
            newPasswd = json.loads(masterPasswdFile.read()).get("password")
            if newPasswd == passwd:
                myPasswords = managePasswords.managePassword(self.__homePath)
                _main(myPasswords)

    def registerUser(self):
        masterPassword = input(
            "Hello! Never saw you here! Please register yourself with a master password.\nPassword: ")
        with open(os.path.join(self.__homePath, MASTER_PASSWORD), "w") as masterPasswdFile:
            newPasswd = json.dumps(
                {
                    "password": masterPassword
                }
            )
            masterPasswdFile.write(newPasswd)
        with open(os.path.join(self.__homePath, OTHER_PASSWORDS), "w") as passwdFile:
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

if __name__ == "__main__":
    init()
