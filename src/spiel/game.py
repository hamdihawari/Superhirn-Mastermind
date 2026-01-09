from src.anwendung import modus
from src.anwendung.spielparameter import Spielparameter
from src.spiel.farbe import Farbe
from src.spiel.spielCodes import Code, Feedback
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from typing import Optional

from src.spiel.strategie.ComputerPlayer import ComputerPlayer
from src.spiel.strategie.MenschPlayer import MenschPlayer


class Game:
    def __init__(self, param: Spielparameter):
        self.modus = param.modus
        self.variante = param.variante
        print("modus.codierer ist = " + self.modus.codierer)

        if self.modus.codierer == "computer":
            try:
                self.codierer = ComputerPlayer(None)
                # Teste die Methode direkt
                test_code = self.codierer.generiereGeheimeCode(self.variante)
                self.secret_code = test_code

                farb_namen = [f.name for f in self.secret_code.farben]
                print(f"Code ist: {farb_namen}")  # Gibt die Liste direkt aus

            except Exception as e:
                print(f"FEHLER: {e}")
                import traceback
                traceback.print_exc()  # Vollständiger Stacktrace
                raise
        else:
            self.codierer = MenschPlayer()
            if param.code is None:
                raise ValueError(f"Im Modus {self.modus.name} muss ein Code übergeben werden!")
            self.secret_code = param.code

        # Rater initialisieren
        if self.modus.rater == "computer":
            self.rater = ComputerPlayer(param.algorithmus)
        else:
            self.rater = MenschPlayer()

        self.runden: list[SpielRunde] = []
        self.erfolgreich = False

    def fuehreRateversuchDurch(self,code:Code) -> Feedback:
        if self.rater == "computer":
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

        print("-------im Game Layer - Feedback ----------")
        print(f"so sieht der geratete Code aus : {geheim}")
        print(f"so sieht der geratete Code aus : {geraten}")

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


