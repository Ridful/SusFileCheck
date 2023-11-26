
from sys import argv, exit
from application.utils.paths import get_filename_and_fullpath # Filename_Path_Controller, get_filename_and_fullpath
from pathlib import Path
from application.operations.inspector import Inspector
from application.operations.director import Director
from application.operations.reporter import Reporter
from typing import List


def main(filename_to_check: str):
    
    filename, full_filepath = get_filename_and_fullpath(filename_to_check)

    director = Director()
    
    reporter = Reporter()
    inspector = Inspector(filename, full_filepath)
    
    director.reporter = reporter
    director.inspector = inspector
    
    alerts_result = list(director.inspector.runChecks()) or []
    if isinstance(alerts_result, list):
        print(alerts_result)
        director.reporter.addAlerts("filechecks", list(alerts_result))
    
    print(f"amt_fileExt: {len(director.inspector.targetFileExts)}")
    print(f"file extensions: {director.inspector.targetFileExts}")
    
    #print(director.reporter.Suspect_Findings_Log)


if __name__ == "__main__":
    assert len(argv) == 2 and type(argv[1] is str), f"Syntax: \"python run.py filename.ext\"."
    main(argv[1])