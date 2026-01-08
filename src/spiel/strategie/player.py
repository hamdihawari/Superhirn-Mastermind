from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING


from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.variante import Variante


class Player(ABC):


    @abstractmethod
    def generiereGeheimeCode(self, variante: Variante) -> Code:
        pass

    @abstractmethod
    def generiereVersuch(self, runden: list[SpielRunde]) -> Code:
        pass