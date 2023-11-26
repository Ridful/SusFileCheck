
from application.utils.ui import *
#import the dict of logs and severity

class Reporter:
    """Accepts the inspectors reports, logs, labels and reports to director on request"""
    
    Suspect_Findings_Log: dict[str, list()] = {}
    
    def __init__(self):
        pass
    
    def addAlerts(self, alertCategory:str, alerts:list()):
        
        self.Suspect_Findings_Log.update({alertCategory: alerts})
        print(f"Added Alert: {alertCategory} | {alerts}")
        
        #print(f"Full Suspect_Findings_Log: \"{self.Suspect_Findings_Log}\".")
        
    def getSuspectFindingsLog(self):
        return self.Suspect_Findings_Log