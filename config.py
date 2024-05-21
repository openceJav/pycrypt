import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load .env File
load_dotenv(os.path.join(BASE_DIR, ".env"))

TOP_LEVEL_DIR = os.path.abspath(os.curdir)


class Config(object):
    DEBUG = False