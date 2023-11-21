import os
#from typing import Union
from pathlib import Path

class Filename_Path_Controller:
    def __init__(self, filename, filename_full_path):
        self.filename = filename
        self.filename_full_path = filename_full_path
    
    def is_valid_windows_filename(self):
        # Check if the filename is valid in Windows
        #base_filename = os.path.basename(targetFileName)
        
        #windows_filename_pattern = re.compile(r'^[^<>:"/\\|?*]+$')
        
        #if not windows_filename_pattern.match(base_filename):
        #    print(f"The filename '{base_filename}' is not valid in Windows.")
        #    return False
        
        #if is_valid_windows_filename(targetFile) is not True:
        #log about blabla bla
        pass

    def has_multiple_FileExtensions(self):
        parts = self.filename.split(".")
        if len(parts) >= 3:
            #add alert
            print(f"Yikes! {parts}")      
    
def get_filename_and_fullpath(file_or_filepath: str):
    # Convert the input to a Path object
    path_obj = Path(file_or_filepath)

    # Check if the input is a full path
    if path_obj.is_absolute():
        full_path = path_obj
    else:
        # Combine current location with the provided filename
        #full_path = Path.cwd() / path_obj
        full_path = Path.cwd().joinpath(path_obj)
        print(full_path)

    # Extract the filename from the full path
    filename = full_path.name

    # Check if the file exists
    if full_path.exists():
        return filename, str(full_path)
    else:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")

