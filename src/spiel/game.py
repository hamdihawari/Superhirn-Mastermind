from src.anwendung import modus
from src.anwendung.spielparameter import Spielparameter
from src.spiel.farbe import Farbe
from src.spiel.spielCodes import Code, Feedback
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from typing import Optional

from src.spiel.strategie.playerType import ComputerPlayer, HumanPlayer


class Game:
    def __init__(self,param:Spielparameter):
        self.modus = param.modus
        self.variante=param.variante
        if self.modus.codierer == "computer":
            self.codierer = ComputerPlayer(param.algorithmus)
            self.secret_code=self.codierer.generiereGeheimeCode(param.variante)
        else:
            self.codierer=HumanPlayer()
            self.secret_code=param.code
        if self.modus.rater == "computer":
            self.rater = ComputerPlayer(param.algorithmus)
        else:
            self.rater=HumanPlayer()
        self.runden: list[SpielRunde] = []
        self.erfolgreich = False

    def fuehreRateversuchDurch(self,code:Code) -> Feedback:
        if self.modus.rater == "computer":
            code=self.rater.generiereVersuch(self.runden)
        feedback = self.berechneFeedback(code)
        erfolgreich = feedback.schwarz == self.variante.steckplaetze

        runde = SpielRunde(
            code=code,
            feedback=feedback,
            rundenNr=len(self.runden) + 1,
            erfolgreich=erfolgreich
        )
        self.runden.append(runde)
        self.istFertig()
        return feedback

    def istFertig(self) -> bool:
        return any(r.erfolgreich for r in self.runden) or \
               len(self.runden) >= self.variante.maxVersuche



    #Hilfsmethode für fuehreRateversuchDurch

    def berechneFeedback(self, rate_code: Code) -> Feedback:
        # Listen mit Optional[Farbe] erstellen
        geheim: list[Optional[Farbe]] = list(self.secret_code.farben)
        geraten: list[Optional[Farbe]] = list(rate_code.farben)

        schwarz = 0
        weiss = 0

        for i in range(len(geheim)):
            if geraten[i] == geheim[i]:
                schwarz += 1
                geheim[i] = None
                geraten[i] = None

        for i in range(len(geraten)):
            if geraten[i] is not None and geraten[i] in geheim:
                weiss += 1
                index = geheim.index(geraten[i])
                geheim[index] = None

        return Feedback(schwarz, weiss)


