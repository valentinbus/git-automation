import sys
import os
import subprocess
import requests
import logging
import json


logging.basicConfig(level=logging.DEBUG)

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
    cmd = f"sh .gitinit.sh {folder_name}"

    
    try:
        #os.makedirs(PATH+folder_name)
        os.system(cmd)
    except FileExistsError:
        logging.debug("You have to remove your existing folder first")

    return "Success creation folder"

if __name__ == "__main__":
    create_repo()
