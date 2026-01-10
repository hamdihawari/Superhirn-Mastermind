from __future__ import annotations

import random
from typing import List

from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class ComputerPlayer(Player):
    def __init__(self, algorithmus_name: str | None = None):
        self.algorithmus = algorithmus_name
        print(" --- COMPUTER PLAYER INITIALIZATION ---")

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

    def generiereVersuchMitVariante(
            self,
            runden: List[SpielRunde],
            variante: Variante
    ) -> Code:

        if self.algorithmus is None:
            raise ValueError("ComputerPlayer hat keinen Algorithmus!")

        return self.algorithmus.berechneNaechstenVersuch(runden, variante)

