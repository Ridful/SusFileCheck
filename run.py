#from application import SuspectorMain
from sys import argv, exit

if __name__ == "__main__":
    
    assert len(argv) == 2 and type(argv[1] is str), f"Syntax: \"python run.py filename.ext\"."
    
    from application.main import main
    main(argv[1])
    
    exit()