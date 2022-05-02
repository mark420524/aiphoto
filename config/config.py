import configparser
import os

config = configparser.ConfigParser()
parent_folder = os.path.dirname(os.path.dirname(__file__))
config_file = os.path.join(parent_folder, 'config.ini')
config.read(config_file, encoding="utf-8")


def get_config(base_key):
    return config[base_key]
