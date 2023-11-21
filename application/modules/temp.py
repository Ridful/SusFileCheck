from application.utils.ui import Status



def _is_valid_windows_filename(self):
        pass

def _has_multiple_FileExtensions(self):
    parts = self.filename.split(".")
    if len(parts) >= 3:
        #print(f"Yikes! {parts}")
        return Status.Warning

def _is_RTLO_present(self):
    pass

def _isFileExtensionNativeExecutable(self):
    #query the registry to see which file extensions can be ran like exes on this win system.
    pass

def _is_ext_lnk(self):
    pass

def _is_archived(self):
    pass

def _is_openxml_archive(self):
    pass
    
#read the file magic
#does file magic match with file extension
#does the lnk have any additional startup params
#has_mark_of_the_web ?
#highlight_non-latins
#highlight_non-locale-characters in filename
#is signed?
#get hashsums  