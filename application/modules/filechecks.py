from application.utils.ui import Status

RTLO_CHARACTER = '\u202E'
ARCHIVE_EXT = ['zip', 'tar', 'tar.gz', 'tar.bz2', 'tar.xz', 'rar', '7z', 'gz', 'zipx']
LNK_EXT = 'lnk'
OPENXML_ARCHIVE_EXT = ['pptx', '.xlsx', '.docx']
ALT_EXECUTABLE_EXT = ['com', 'cmd', 'scr', 'bat', 'vbs', 'vbe', 'wsf', 'msc', 'wsh']
ISO_EXT = 'iso'


def _is_valid_windows_filename(self):
    pass

def _has_multiple_FileExtensions(self):
    parts = self.targetFileName.split(".")
    if len(parts) >= 3:
        #print(f"Yikes! {parts}")
        return Status.Warning

def _is_RTLO_present(self):
    if RTLO_CHARACTER in self.targetFileName:
        print(f"The RTLO Character: {RTLO_CHARACTER} was found in: \"{self.targetFileName}\"!")
        print(f"utf-8 decoded: {self.targetFileName.encode('unicode_escape').decode("utf-8")}")
        return Status.Danger

def _is_lnk_ext(self):
    if any(LNK_EXT in str(fileExt).lower() for fileExt in self.targetFileExts):
        #print("Found .lnk as file extensions")
        return Status.Info

def _is_iso_ext(self):
    if any(ISO_EXT in str(fileExt).lower() for fileExt in self.targetFileExts):
        return Status.Info

def _is_archived(self):
    targetFileExtsLower = [fileExt.lower() for fileExt in self.targetFileExts]
    #print(targetFileExtsLower)
    matches = [item for item in targetFileExtsLower if item in ARCHIVE_EXT]

    if matches:
        print(f"Found Matching Archive Extensions: {matches}")
        return Status.Info
    else:
        return None

#def _is_archived(self):
    #if 
    #pass

def _is_openxml_archive(self):
    pass

def _isFileExtensionNativeExecutable(self):
    #query the registry to see which file extensions can be ran like exes on this win system.
    pass

#read the file magic
#does file magic match with file extension
#does the lnk have any additional startup params
#has_mark_of_the_web ?
#highlight_non-latins
#highlight_non-locale-characters in filename
#is signed?
#get hashsums  