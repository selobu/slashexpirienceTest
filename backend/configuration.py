# coding:utf-8
__all__ = ["config", "saveConfig"]

from configparser import ConfigParser
import os.path
from os import getcwd
from pathlib import Path

dir_path = Path(getcwd())
config_filepath = os.path.join(dir_path, "config.ini")

# check if the config file exists
exists = os.path.exists(config_filepath)
config = ConfigParser()
if exists:
    config.read(config_filepath)
else:
    default = {"MAX_POSITION_ALLOWED": "61695", "MAX_TRIES": "16"}
    config.add_section("general")
    for key, value in default.items():
        config.set("general", key, value)
    fp = open(config_filepath, "w")
    config.write(fp)
    fp.close()


def saveConfig(config):
    fp = open(config_filepath, "w")
    config.write(fp)
