import random
from typing import List, Set, Tuple
from src.spiel.spielCodes import Code
from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.variante import Variante
from src.spiel.farbe import Farbe
from src.spiel.spielCodes import Feedback
from itertools import product


class Knuth(AlgorithmusStrategie):
    def __init__(self):
        # Wir halten für jede Variante eine Liste aller möglichen Codes
        self.candidate_cache: dict[Variante, List[Code]] = {}

    def berechneNaechstenVersuch(self, runden: List["SpielRunde"], variante: Variante) -> Code:
        # Kandidatenliste initialisieren, falls noch nicht geschehen
        if variante not in self.candidate_cache:
            self.candidate_cache[variante] = [
                Code(list(p)) for p in product(variante.erlaubteFarben, repeat=variante.steckplaetze)
            ]

        candidates = self.candidate_cache[variante]

        # Ersten Versuch nach Knuth-Strategie
        if not runden:
            farben = list(variante.erlaubteFarben)
            if len(farben) >= 2 and variante.steckplaetze >= 4:
                start = [farben[0], farben[0], farben[1], farben[1]]
                while len(start) < variante.steckplaetze:
                    start.append(farben[0])
                return Code(start[:variante.steckplaetze])
            return Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))

        # Letzten Versuch prüfen
        letzter_versuch = runden[-1].code
        feedback: Feedback = runden[-1].feedback

        # Kandidaten filtern: Nur Codes behalten, die mit dem Feedback kompatibel sind
        candidates = [
            c for c in candidates if self._passt_feedback(c, letzter_versuch, feedback)
        ]
        self.candidate_cache[variante] = candidates

        # Nächsten Versuch zufällig aus den Kandidaten
        if candidates:
            return random.choice(candidates)
        else:
            # Fallback, falls keine Kandidaten übrig
            return Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))

    def _passt_feedback(self, code: Code, guess: Code, feedback: Feedback) -> bool:
        """Prüft, ob ein Code das gleiche Feedback geben würde wie beim letzten Versuch."""
        schwarz, weiss = 0, 0
        guess_farben = list(guess.farben)
        code_farben = list(code.farben)

        # Schwarz zählen
        for i in range(len(code_farben)):
            if code_farben[i] == guess_farben[i]:
                schwarz += 1
                code_farben[i] = guess_farben[i] = None  # Entfernen zur Weiß-Prüfung

        # Weiß zählen
        for i in range(len(guess_farben)):
            if guess_farben[i] and guess_farben[i] in code_farben:
                weiss += 1
                code_farben[code_farben.index(guess_farben[i])] = None

        return schwarz == feedback.schwarz and weiss == feedback.weiss