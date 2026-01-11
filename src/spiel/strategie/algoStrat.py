from abc import ABC, abstractmethod
from typing import List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from src.spiel.game import SpielRunde
    from src.spiel.spielCodes import Code
    from src.spiel.variante import Variante

class AlgorithmusStrategie(ABC):
    @abstractmethod
    def berechneNaechstenVersuch(self, runden: List["SpielRunde"], variante: "Variante") -> "Code":
        pass

class AlgorithmusFactory:
    @staticmethod
    def create(algoTyp: str) -> Union["Knuth", "StepByStep", None]:
        if algoTyp == "knuth":
            from spiel.strategie.algorithmen.knuth import Knuth
            return Knuth()
        elif algoTyp == "step_by_step":
            from spiel.strategie.algorithmen.step_by_step import StepByStep
            return StepByStep()
        else:
            return None
