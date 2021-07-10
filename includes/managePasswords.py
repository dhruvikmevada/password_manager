import json
from os import path
from . import check

OTHER_PASSWORD = check.OTHER_PASSWORDS
d_main = {1: "instagram", 2: "facebook", 3: "twitter", 4: "gmail", 5: "outlook"}


class ManagePassword:
    def __init__(self, home_path):
        self.__homePath = home_path
        self.passwordFile = path.join(self.__homePath, OTHER_PASSWORD)
        print(
            "\nAvailable domains are:\n\n1. Instagram\n2. Facebook\n3. Twitter\n4. Gmail\n5. Outlook"
        )
        self.askDomain = input("Your choice: ")
        self.add_password = eval(open(self.passwordFile, "r").read())

    def add_passwords(self):
        ask_username = input("\nUsername: ")
        ask_password = input("Password: ")
        pass_list = self.add_password.get(d_main.get(int(self.askDomain)))

        pass_list.append({"username": ask_username, "password": ask_password})
        self.add_password[d_main[int(self.askDomain)]] = pass_list
        with open(self.passwordFile, "w") as pwdFile:
            pwdFile.write(json.dumps(self.add_password))

    def get_passwords(self):
        ask_username = input("\nUsername: ")
        uname_list = self.add_password.get(d_main.get(int(self.askDomain)))
        # print(unameList)
        for uKey in uname_list:
            # print(uKey)
            if uKey["username"] == ask_username:
                print(f"\nYour password for {ask_username} is: {uKey['password']}")
                break
            else:
                print("\nNo username found!")
                break
