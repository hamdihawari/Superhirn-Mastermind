from __future__ import annotations

import random
from typing import List

from spiel.strategie.algoStrat import AlgorithmusFactory
from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class ComputerPlayer(Player):
    def __init__(self, algorithmus_name: str | None = None):
        self.algo = AlgorithmusFactory.create(algorithmus_name)

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

        if self.algo is None:
            raise ValueError("ComputerPlayer hat keinen Algorithmus!")

        return self.algo.berechneNaechstenVersuch(runden, variante)

