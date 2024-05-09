import os


def remove_files(target_dir):
    for root, directories, files in os.walk(target_dir):
        for file in files:
            os.remove(os.path.join(root, file))