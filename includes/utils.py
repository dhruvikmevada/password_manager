import os
import sys

MASTER_PASSWORD = ".masterpwd.json"
OTHER_PASSWORDS = ".password_manager.json"


def os_type():
    return sys.platform


def is_pwd_set(home_path, passwd_file):
    dir_list = os.listdir(home_path)
    if passwd_file in dir_list:
        return True
    return False


def get_env(env_key):
    return os.environ.get(env_key)
