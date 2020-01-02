import sys
import os
import subprocess
import requests
import logging
import json
import time


logging.basicConfig(level=logging.DEBUG)

BASE_URL="https://api.github.com/"
CREATE_REPO_URL="https://api.github.com/user/repos"
DELETE_REPO_URL="https://api.github.com/repos"
PATH = "/Users/valentinbus/Documents/repo/"
USERNAME = "valentinbus"
TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")


def create_repo():
    """
    Create and init repo on github
    """
    repo_name = str(sys.argv[1])

    body = {
        "name": repo_name
    }

    requests.post(
        CREATE_REPO_URL,
        auth=(USERNAME, TOKEN),
        data=json.dumps(body)
    )

    init_local_folder(repo_name)

def init_local_folder(folder_name):
    """
    Create and init local folder
    """
    time.sleep(2)
    cmd = f"sh /Users/valentinbus/Documents/repo/git-automation/.gitinit.sh {folder_name}"

    try:
        os.makedirs(PATH+folder_name)
    except FileExistsError:
        logging.debug("You have to remove your existing folder first")

    os.system(cmd)
    
    return "Success creation folder"


if __name__ == "__main__":
    create_repo()
