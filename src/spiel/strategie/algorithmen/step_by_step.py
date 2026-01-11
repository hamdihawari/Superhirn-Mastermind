from __future__ import annotations

from itertools import product
from typing import List, TYPE_CHECKING, Optional, Set, Tuple

from src.spiel.farbe import Farbe
from src.spiel.spielCodes import Code, Feedback
from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.variante import Variante

if TYPE_CHECKING:
    from src.spiel.spielrunde import SpielRunde

def eval_feedback(secret: Code, guess: Code) -> Feedback:
    geheim: list[Optional[Farbe]] = list(secret.farben)
    geraten: list[Optional[Farbe]] = list(guess.farben)

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
            idx = geheim.index(geraten[i])
            geheim[idx] = None

    return Feedback(schwarz, weiss)

def all_codes(variante: Variante) -> list[Code]:
    farben = list(variante.erlaubteFarben)
    return [Code(p) for p in product(farben, repeat=variante.steckplaetze)]

class StepByStep(AlgorithmusStrategie):
    def __init__(self):
        self._key = None
        self._space: list[Code] = []

    def _ensure_space(self, variante: Variante):
        key = (tuple(variante.erlaubteFarben), variante.steckplaetze)
        if key != self._key:
            self._key = key
            self._space = all_codes(variante)

    def berechneNaechstenVersuch(self, runden: List[SpielRunde], variante: Variante) -> Code:
        self._ensure_space(variante)
        used: Set[Tuple] = {tuple(r.code.farben) for r in runden}
        candidates = self._space
        for r in runden:
            fb = r.feedback
            guess = r.code
            candidates = [
                s for s in candidates
                if (eval_feedback(s, guess).schwarz == fb.schwarz and
                    eval_feedback(s, guess).weiss == fb.weiss)
            ]

        print("candidates:", len(candidates))

        for c in candidates:
            if tuple(c.farben) not in used:
                return c
        for c in self._space:
            if tuple(c.farben) not in used:
                return c
        return self._space[0]
