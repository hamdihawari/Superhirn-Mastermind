from __future__ import annotations

import random
from typing import List, TYPE_CHECKING, Set, Tuple

from src.spiel.spielCodes import Code
from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.variante import Variante

if TYPE_CHECKING:
    from src.spiel.spielrunde import SpielRunde

class StepByStep(AlgorithmusStrategie):
    def berechneNaechstenVersuch(self, runden: List[SpielRunde], variante: Variante) -> Code:
        # ًWICHTIG_: Erzeugt schrittweise neue, noch nicht verwendete Codes
        used: Set[Tuple] = set()
        for r in runden:
            used.add(tuple(r.code.farben))
        for _ in range(200):
            guess = Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))
            if tuple(guess.farben) not in used:
                return guess
        return Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))
