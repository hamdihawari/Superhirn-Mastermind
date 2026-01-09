from __future__ import annotations

from typing import List, Optional

from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class MenschPlayer(Player):
    def __init__(self):
        self._next_code: Optional[Code] = None
        self._secret_code: Optional[Code] = None

    def setNextCode(self, code: Code) -> None:
        self._next_code = code

    def setSecretCode(self, code: Code) -> None:
        self._secret_code = code

    def generiereGeheimeCode(self, variante: Variante) -> Code:
        if self._secret_code is None:
            raise ValueError("MenschPlayer: Geheimcode wurde nicht gesetzt (setSecretCode(...) aufrufen).")
        return self._secret_code

    def generiereVersuch(self, runden: List[SpielRunde]) -> Code:
        if self._next_code is None:
            raise ValueError("MenschPlayer: Rateversuch wurde nicht gesetzt (setNextCode(...) aufrufen).")

        code = self._next_code
        self._next_code = None
        return code
