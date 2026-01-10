from abc import ABC
from src.anwendung.spielparameter import Spielparameter, Modus
from src.kommunikation.comPort import ComPort
from src.spiel.game import Game
from src.spiel.spielCodes import Feedback
from src.spiel.spielCodes import Code


class EngineInt(ABC):

    def fuehreZugAus(self,code:Code)->Feedback:
        pass

    def istFertig(self)->bool:
        pass

class SpielEngine(EngineInt):

    def __init__(self,param:Spielparameter):
        self.spiel = Game(param)
        self.modus = param.modus
        self.com = ComPort()
        if param.modus.online:
            self.com.starte(param.variante)
            self.runde =0

    def fuehreZugAus(self,code:Code)->Feedback:
        if self.modus == Modus.C_M_ONLINE  or self.modus == Modus.C_C_ONLINE:
            self.runde+=1
            return self.com.sendeVersuch(code)
        return self.spiel.fuehreRateversuchDurch(code)

    def istFertig(self)->bool:
        if self.modus.online:
            return self.runde >= self.spiel.variante.maxVersuche
        return self.spiel.istFertig()


