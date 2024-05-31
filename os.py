import os
import shutil
from pathlib import Path
import inspect


def make_dir(new_dir, force=False):
    new_dir = os.path.join(*new_dir)
    print(new_dir)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        return new_dir
    
    if os.path.exists(new_dir):
        if force == True:
            remove_dir(new_dir)
            
            os.makedirs(new_dir)
            return new_dir
        else:
            raise FileExistsError(f"The directory '{new_dir}' already exists. You can use force=True if you want to remove and create.")
        
    

def remove_dir(rm_dir):
    if os.path.exists(rm_dir):
        shutil.rmtree(rm_dir)


def copy_dir(source_dir, target_dir):
    pass


def current_file_dir():
    frame = inspect.stack()[1]
    caller_file = frame.filename
    current_path = Path(caller_file).resolve()
    current_dir = current_path.parent
    return (current_dir, current_path)