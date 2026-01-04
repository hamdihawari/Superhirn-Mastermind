from abc import ABC, abstractmethod
from typing import List

from src.spiel.game import spielRunde
from src.spiel.spielCodes import Code
from src.spiel.variante import Variante


class AlgorithmusStrategie(ABC):

    @abstractmethod
    def berechneNaechstenVersuch(runden:List[spielRunde],variante:Variante) -> Code :
        pass