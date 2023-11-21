

class Status:
    """Indicates the response status of a request or action"""
    
    Success = "success"
    Danger = "danger"
    Error = "error"  # Alias #danger
    Warning = "warning"
    Info = "info"
    Alert = "alert"
    Critical = "critical"


def log(text: str, status: str = ""):
    """Log important information to the console"""
    style = ""
    if status == Status.Info:
        style = "blue"
    elif status == Status.Success:
        style = "green"
    elif status == Status.Warning:
        style = "yellow"
    elif status == Status.Danger:
        style = "red"
    elif status == Status.Critical:
        style = "#ff0000"
    
    print("[" + status.upper() + "] " + "|" + style + "| " + text)
    #console.print("[" + status.upper() + "] " + text, style=style)
    

def pretty_print(text: str, force: bool = False):
    #print(Colorate.Horizontal(Colors.yellow_to_red, text))
    pass