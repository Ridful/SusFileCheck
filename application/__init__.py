import os
import re

class HSE_File_Suspector:
    
    SussyFindingsLog: dict[str, list()] = None
    
    def __init__(self, targetFileName, targetFilePath):
        pass

def is_valid_windows_filename(targetFileName: str):
    """
    Check if a filename is both valid and exists in a Windows environment.

    Args:
    - filename (str): The name of the file to check.

    Returns:
    - bool: True if the file is valid and exists, False otherwise.
    """
    
    # Get the current working directory
    current_location = os.getcwd()
    
    # Check if the filename is already a full path
    if os.sep in targetFileName:
        full_path = targetFileName
    else:
        # Combine current location with the provided filename
        full_path = os.path.join(current_location, targetFileName)
    
    # Check if the file exists
    if not os.path.exists(full_path):
        print(f"The file '{full_path}' does not exist or wasn't found.")
        return False

    # Check if the filename is valid in Windows
    base_filename = os.path.basename(targetFileName)
    windows_filename_pattern = re.compile(r'^[^<>:"/\\|?*]+$')
    
    if not windows_filename_pattern.match(base_filename):
        print(f"The filename '{base_filename}' is not valid in Windows.")
        return False

    print(f"base_filename: {base_filename}")
    return True

def SuspectorMain(targetFile: str):
    
    FileSusser = HSE_File_Suspector()
    
    if is_valid_windows_filename(targetFile) is not True:
        raise FileNotFoundError ("Cant find provided targetFile")
    
    
    
    