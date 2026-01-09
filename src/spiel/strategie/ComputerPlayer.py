from __future__ import annotations

import random
from typing import List

from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class ComputerPlayer(Player):
    def __init__(self, algorithmus: str):
        self.algorithmus = algorithmus

    def generiereGeheimeCode(self, variante: Variante) -> Code:
        print(f"test")
        return Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))

    def generiereVersuch(self, runden: List[SpielRunde]) -> Code:
        raise NotImplementedError(
            "ComputerPlayer: Bitte generiereVersuchMitVariante(runden, variante) verwenden."
        )

    def generiereVersuchMitVariante(self, runden: List[SpielRunde], variante: Variante) -> Code:
        return self.algorithmus.berechneNaechstenVersuch(runden, variante)
