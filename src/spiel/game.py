from typing import List

from src.spiel.spielCodes import Code, Feedback
from src.spiel.strategie import player
from src.spiel.variante import Variante


class game:
    def __init__(self,codierer:player, rater:player,variante:Variante,secretCode:Code):
        self.codierer=codierer
        self.rater=rater
        self.variante=variante
        self.secretCode=secretCode
        self.runden=List[spielRunde] = []

    def fuehreRateversuchDurch(code:Code) -> Feedback:
        pass

    def istFertig(self) -> bool:
        pass

class spielRunde:
    def __init__(self,code:Code,feedback:Feedback,rundenNr:int,erfolgreich:bool):
        self.code=code
        self.feedback=feedback
        self.rundenNr=rundenNr
        self.erfolgreich=erfolgreich

