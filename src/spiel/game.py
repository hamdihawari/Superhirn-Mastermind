from anwendung.modus import Modus
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

        # Codierer initialisieren (Computer oder Mensch)
        if self.modus.codierer == "computer":
            try:
                self.codierer = ComputerPlayer(None)
                test_code = self.codierer.generiereGeheimeCode(self.variante)
                self.secret_code = test_code
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

    def fuehreRateversuchDurch(self,code:Code | None) -> Feedback:

        # Computer generiert eigenen Rateversuch
        if self.modus.rater == "computer":
            code=self.rater.generiereVersuchMitVariante(self.runden,self.variante)

        # Feedback berechnen
        feedback = self.berechneFeedback(code)
        erfolgreich = feedback.schwarz == self.variante.steckplaetze

        # Runde speichern
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
        # Spiel endet bei Erfolg oder maximaler Rundenzahl
        return any(r.erfolgreich for r in self.runden) or \
               len(self.runden) >= self.variante.maxVersuche



    #Hilfsmethode für fuehreRateversuchDurch
    # Berechnet schwarzes und weißes Feedback
    def berechneFeedback(self, rate_code: Code) -> Feedback:
        # Listen mit Optional[Farbe] erstellen
        geheim: list[Optional[Farbe]] = list(self.secret_code.farben)
        geraten: list[Optional[Farbe]] = list(rate_code.farben)

        schwarz = 0
        weiss = 0

        # Schwarze Treffer (richtige Farbe, richtige Position)
        for i in range(len(geheim)):
            if geraten[i] == geheim[i]:
                schwarz += 1
                geheim[i] = None
                geraten[i] = None

        # Weiße Treffer (richtige Farbe, falsche Position)
        for i in range(len(geraten)):
            if geraten[i] is not None and geraten[i] in geheim:
                weiss += 1
                index = geheim.index(geraten[i])
                geheim[index] = None

        return Feedback(schwarz, weiss)


