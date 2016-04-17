import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GITHUB_API_USER = os.environ.get("GITHUB_API_USER")
GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")
