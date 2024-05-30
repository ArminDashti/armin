# This code was generated from OpenAI chatGPT 3.5

import subprocess


def clone_repo(repo_url, destination_path):
    subprocess.check_output(['git', 'clone', repo_url, destination_path])
    print("Repository cloned successfully.")
