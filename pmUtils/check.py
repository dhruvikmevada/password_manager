import os
import sys


def osType():
    return sys.platform

def isPwdSet(homePath, passwdFile):
    dirList = os.listdir(homePath)
    if passwdFile in dirList:
        return True
    return False

def getEnv(envKey):
    return os.environ.get(envKey)
