import logging
import sys
logfile = "result.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s  %(pathname)s line:%(lineno)d  %(levelname)s : %(message)s thread:%(thread)d',
                    datefmt=' %Y-%m-%d %H:%M:%S',
                    stream=sys.stdout)


def get_log():
    return logging
