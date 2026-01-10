from __future__ import annotations

import random
from typing import List, TYPE_CHECKING, Set, Tuple

from src.spiel.spielCodes import Code
from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.variante import Variante

if TYPE_CHECKING:
    from src.spiel.spielrunde import SpielRunde


class Knuth(AlgorithmusStrategie):
    def berechneNaechstenVersuch(self, runden: List[SpielRunde], variante: Variante) -> Code:
        used: Set[Tuple] = {tuple(r.code.farben) for r in runden}

        if not runden:
            farben = list(variante.erlaubteFarben)
            if len(farben) >= 2 and variante.steckplaetze >= 4:
                start = [farben[0], farben[0], farben[1], farben[1]]
                while len(start) < variante.steckplaetze:
                    start.append(farben[0])
                return Code(start[:variante.steckplaetze])

            return Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))

        for _ in range(500):
            guess = Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))
            if tuple(guess.farben) not in used:
                return guess
        code = Code(random.choices(variante.erlaubteFarben, k=variante.steckplaetze))
        return code
