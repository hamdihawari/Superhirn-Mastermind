from enum import Enum

class Modus(Enum):
    M_C=("mensch","computer",False)
    C_M=("computer","mensch",False)
    C_C=("computer","computer",False)
    C_M_ONLINE=("computer_online","mensch",True)
    C_C_ONLINE=("computer_online","computer",True)

    def __init__(self,codierer,rater,online:bool):
        self.codierer=codierer
        self.rater = rater
        self.online=online