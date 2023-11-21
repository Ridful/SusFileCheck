#from application.utils.paths import Filename_Path_Controller
from application.utils.ui import log, Status
#Sus_dictionary_reference = {
#    "has_multiple_FileExtensions": "",
#   "RTLO": "blabla",
#   "Archive/ISO", "bad because allows alot of bypass of filters, detections, defender, motw, etc"
#}


class Inspector:
    """Runs and checks the various aspects of the target file"""
    
    from application.modules.temp import _has_multiple_FileExtensions
    
    def __init__(self, targetFileName: str, targetFilePath):
        
        self.targetFileName = targetFileName
        self.targetFilePath = targetFilePath


    def runChecks(self):
        
        checks_catalogue = {
            "MultipleFileExtensions": self._has_multiple_FileExtensions
        }
        
        for check_name, check_method in checks_catalogue.items():
            #res: Status.Error = check_method(self)
            res = check_method()
            print(f"{res} - {check_method()}")
            log(status=res, text=f"{check_name} got triggered!")
            return res
    
    def log_sus_alarm(self, info):
        #log(log_msg, status_str)
        pass