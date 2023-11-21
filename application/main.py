
from sys import argv, exit
from application.utils.paths import get_filename_and_fullpath # Filename_Path_Controller, get_filename_and_fullpath
from pathlib import Path
from application.operations.inspector import Inspector
from application.operations.director import Director
from application.modules.temp import _has_multiple_FileExtensions

def main(filename_to_check: str):
    
    filename, full_filepath = get_filename_and_fullpath(filename_to_check)

    director = Director()
    
    #FilePathControl = Filename_Path_Controller(filename, full_filepath)
    inspector = Inspector(filename, full_filepath)
    
    inspector.runChecks()
    
    #director.inspector = inspector
    #director.reporter = reporter
    
    #director.inspector.runChecks()
    

    #FilePathControl.get_Path_CWD()
    #FilePathControl.filename_full_path()
    #FilePathControl.has_multiple_FileExtensions()
    #inspector._has_multiple_FileExtensions()


if __name__ == "__main__":
    assert len(argv) == 2 and type(argv[1] is str), f"Syntax: \"python run.py filename.ext\"."
    main(argv[1])