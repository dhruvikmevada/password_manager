import json
from os import path
from . import check

OTHER_PASSWORD = check.OTHER_PASSWORDS
dmain = {1: "instagram", 2: "facebook", 3: "twitter", 4: "gmail", 5: "outlook"}


class managePassword:
    def __init__(self, homePath):
        self.__homePath = homePath
        self.passwordFile = path.join(self.__homePath, OTHER_PASSWORD)
        print(
            "\nAvailable domains are:\n\n1. Instagram\n2. Facebook\n3. Twitter\n4. Gmail\n5. Outlook"
        )
        self.askDomain = input("Your choice: ")
        self.add_password = eval(open(self.passwordFile, "r").read())

    def addPasswords(self):
        askUsername = input("\nUsername: ")
        askPassword = input("Password: ")
        passList = self.add_password.get(dmain.get(int(self.askDomain)))

        passList.append({"username": askUsername, "password": askPassword})
        self.add_password[dmain[int(self.askDomain)]] = passList
        with open(self.passwordFile, "w") as pwdFile:
            pwdFile.write(json.dumps(self.add_password))

    def getPasswords(self):
        askUsername = input("\nUsername: ")
        unameList = self.add_password.get(dmain.get(int(self.askDomain)))
        # print(unameList)
        for uKey in unameList:
            # print(uKey)
            if uKey["username"] == askUsername:
                print(f"\nYour password for {askUsername} is: {uKey['password']}")
                break
            else:
                print("\nNo username found!")
                break
