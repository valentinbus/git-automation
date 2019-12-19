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


def delete_repo():
    """
    Create and init repo on github
    """
    repo_name = str(sys.argv[1])

    body = {
        "name": repo_name
    }

    requests.delete(
        f"{DELETE_REPO_URL}/{USERNAME}/{repo_name}",
        auth=(USERNAME, TOKEN)
    )

    delete_local_folder(repo_name)

def delete_local_folder(folder_name):
    """
    Create and init local folder
    """
    cmd = f"sh .gitdelete.sh {folder_name}"
    os.system(cmd)

if __name__ == "__main__":
    delete_repo()
