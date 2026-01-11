from abc import ABC, abstractmethod

from kommunikation.comPort import ComJson
from spiel.spielrunde import SpielRunde
from spiel.strategie.algorithmen.knuth import Knuth
from src.anwendung.spielparameter import Spielparameter
from src.anwendung.modus import Modus
from src.kommunikation.comPort import ComPort
from src.spiel.game import Game
from src.spiel.spielCodes import Feedback
from src.spiel.spielCodes import Code


class EngineInterface(ABC):

    @abstractmethod
    def fuehreZugAus(self,code:Code)->Feedback:
        pass

    @abstractmethod
    def istFertig(self)->bool:
        pass

    @abstractmethod
    def letzteRunde(self):
        pass

class SpielEngine(EngineInterface):

    def __init__(self,param:Spielparameter):
        self.modus = param.modus
        self.variante = param.variante
        if not self.modus.online:
            self.spiel = Game(param)
        self.com :ComPort
        # self.runde = 0
        #falls Online-Modus, dann wird ComPort gestartet
        if param.modus.online:
            self.com=ComJson()
            self.com.starte(param.variante)
            self.runde =0
            self.algo = Knuth()
            self.spielrunde: list[SpielRunde] = []


    #gibt den Sendeversuch and SpielLayer oder Comlayer weiter
    def fuehreZugAus(self,code:Code)->Feedback:
        if self.modus.online:
            self.runde += 1
            if self.modus.rater == "mensch":
                return self.com.sendeVersuch(code)
            else:
                farbencode = self.algo.berechneNaechstenVersuch(self.spielrunde, self.variante)
                feedback = self.com.sendeVersuch(farbencode)
                self.spielrunde.append(SpielRunde(farbencode,feedback,self.runde, False))
                return feedback
        return self.spiel.fuehreRateversuchDurch(code)

    #prüft bei Online-Modus ob Spiel maxVersuche erreicht hat, und bei Offline gibt es weiter an SpielLayer
    def istFertig(self)->bool:
        if self.modus.online:
            return self.runde >= self.variante.maxVersuche
        return self.spiel.istFertig()

    def letzteRunde(self):
        if self.modus.online:
            return self.spielrunde[-1]
        return self.spiel.runden[-1]


class VergleichsEngine(EngineInterface):

    def __init__(self, engine_a: EngineInterface, engine_b: EngineInterface):
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
        return self.engine_a.istFertig() or self.engine_b.istFertig()

    def letzteRunde(self):
        return {
            "A": self.engine_a.letzteRunde(),
            "B": self.engine_b.letzteRunde()
        }


