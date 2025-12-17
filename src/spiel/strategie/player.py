from abc import ABC, abstractmethod
from typing import List

from src.spiel.game import spielRunde
from src.spiel.spielCodes import Code
from src.spiel.variante import Variante


class Player(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def generiereGeheimeCode(variante:Variante) -> Code:
        pass

    @abstractmethod
    def generiereVersuch(runden:List[spielRunde]) -> Code :
        pass