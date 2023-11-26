from application.utils.ui import log, Status
from typing import List, Union, Dict

class Inspector:
    """Runs and checks the various aspects of the target file"""
    
    from application.modules.filechecks import _has_multiple_FileExtensions
    from application.modules.filechecks import _is_RTLO_present
    from application.modules.filechecks import _is_lnk_ext
    from application.modules.filechecks import _is_iso_ext
    
    def __init__(self, targetFileName: str, targetFilePath):
        
        self.targetFileName = targetFileName
        self.targetFilePath = targetFilePath
        self.targetFileExts = list(targetFileName.split('.')[1::]) #Get a list of all file fileextensions
        print(f"targetFileExts: >>> {self.targetFileExts}")


    def runChecks(self) -> Dict:# -> Union[List[dict()], None]:
        
        print(f"{self.targetFileName}, {self.targetFilePath}")
        
        checks_catalogue = {
            "MultipleFileExtensions": self._has_multiple_FileExtensions,
            "Is_RTLO_Present": self._is_RTLO_present,
            "Is_LNK_EXT": self._is_lnk_ext,
            "Is_ISO_EXT": self._is_iso_ext
        }
        
        for check_name, check_method in checks_catalogue.items():
            #res: Status.Error = check_method(self)
            #res = check_method()
            #print(f"{res} - {check_method()}")
            
            res = check_method()
            
            if isinstance(res, str):
                log(status=check_method(), text=f"{check_name} got triggered!")
                yield {check_name:res}
        
    
    def log_sus_alarm(self, info):
        #log(log_msg, status_str)
        pass