import os
import sys

MASTER_PASSWORD = ".masterpwd.json"
OTHER_PASSWORDS = ".password_manager.json"


def osType():
    return sys.platform


def isPwdSet(homePath, passwdFile):
    dirList = os.listdir(homePath)
    if passwdFile in dirList:
        return True
    return False


def getEnv(envKey):
    return os.environ.get(envKey)
