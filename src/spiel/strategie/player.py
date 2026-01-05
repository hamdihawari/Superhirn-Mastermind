from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

# Nur für Type Hints importieren
if TYPE_CHECKING:
    from src.spiel.game import SpielRunde

from src.spiel.spielCodes import Code
from src.spiel.variante import Variante


class Player(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def generiereGeheimeCode(self, variante: Variante) -> Code:
        pass

    @abstractmethod
    def generiereVersuch(self, runden: List['SpielRunde']) -> Code:  # Als String
        pass