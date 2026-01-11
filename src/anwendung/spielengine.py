from abc import ABC, abstractmethod
from src.anwendung.spielparameter import Spielparameter, Modus
from src.kommunikation.comPort import ComPort
from src.spiel.game import Game
from src.spiel.spielCodes import Feedback
from src.spiel.spielCodes import Code


class EngineInt(ABC):

    @abstractmethod
    def fuehreZugAus(self,code:Code)->Feedback:
        pass

    @abstractmethod
    def istFertig(self)->bool:
        pass

    @abstractmethod
    def letzteRunde(self):
        pass

class SpielEngine(EngineInt):

    def __init__(self,param:Spielparameter):
        self.spiel = Game(param)
        self.modus = param.modus
        self.com = ComPort()
        # self.runde = 0
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

    def letzteRunde(self):
        return self.spiel.runden[-1]


class VergleichsEngine(EngineInt):

    def __init__(self, engine_a: EngineInt, engine_b: EngineInt):
        self.engine_a = engine_a
        self.engine_b = engine_b

        # welche Engine gerade „geführt“ wird
        self.aktive_engine = engine_a

    """
    Führt den Zug in BEIDEN Engines aus.
    Rückgabe ist vorerst das Feedback der aktiven Engine.
    """
    def fuehreZugAus(self, code: Code | None) -> Feedback:

        feedback_a = self.engine_a.fuehreZugAus(code)
        feedback_b = self.engine_b.fuehreZugAus(code)

        self.aktive_engine = self.engine_a

        return feedback_a

    def istFertig(self) -> bool:
        return self.engine_a.istFertig() and self.engine_b.istFertig()

    def letzteRunde(self):
        return {
            "A": self.engine_a.letzteRunde(),
            "B": self.engine_b.letzteRunde()
        }


