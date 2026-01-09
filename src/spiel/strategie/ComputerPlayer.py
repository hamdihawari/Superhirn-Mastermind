from __future__ import annotations

import random
from typing import List

from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class ComputerPlayer(Player):
    def __init__(self, algorithmus_name: str | None = None):
        self.algorithmus = self._erstelleAlgorithmus(algorithmus_name) if algorithmus_name else None

    def generiereGeheimeCode(self, variante: Variante) -> Code:

        if not variante.erlaubteFarben:
            raise ValueError("Keine erlaubten Farben definiert!")

        farben = random.choices(variante.erlaubteFarben, k=variante.steckplaetze)
        code = Code(farben)
        return code

    def generiereVersuch(self, runden: List[SpielRunde]) -> Code:
        raise NotImplementedError(
            "ComputerPlayer: Bitte generiereVersuchMitVariante(runden, variante) verwenden."
        )

    def generiereVersuchMitVariante(self, runden: List[SpielRunde], variante: Variante) -> Code:
        return self.algorithmus.berechneNaechstenVersuch(runden, variante)

