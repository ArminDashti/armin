import os
import shutil
from pathlib import Path
import inspect



def make_dir(dest_dir, force=False):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        return dest_dir
    else:
        if force == True:
            remove_dir(dest_dir)
            os.makedirs(dest_dir)
            return dest_dir
        else:
            raise FileExistsError(f"'{dest_dir}' already exists. You can use force=True if you want to remove and create again.")
        
    
def remove_dir(target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    else:
        raise FileExistsError(f"'{target_dir}' doesn't exists.")


def copy_dir(source_dir, target_dir):
    if (os.path.exists(source_dir)) and (os.path.exists(target_dir)):
        pass
    else:
        raise FileExistsError(f"'{source_dir} or '{target_dir}' doesn't exists.")


copy_file = copy_dir


def current_file_path():
    frame = inspect.stack()[1]
    caller_file = frame.filename
    current_path = Path(caller_file).resolve()
    current_dir = current_path.parent
    return (current_dir, current_path)