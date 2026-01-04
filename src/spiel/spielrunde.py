
from src.spiel.spielCodes import Code,Feedback

class SpielRunde:
    def __init__(self,code:Code,feedback:Feedback,rundenNr:int,erfolgreich:bool):
        self.code=code
        self.feedback=feedback
        self.rundenNr=rundenNr
        self.erfolgreich=erfolgreich