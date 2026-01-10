from abc import ABC, abstractmethod
from typing import List

from spiel.strategie.algorithmen.knuth import Knuth
from spiel.strategie.algorithmen.step_by_step import StepByStep
from src.spiel.game import SpielRunde
from src.spiel.spielCodes import Code
from src.spiel.variante import Variante


class AlgorithmusStrategie(ABC):

    @abstractmethod
    def berechneNaechstenVersuch(self,runden:List[SpielRunde],variante:Variante) -> Code :
        pass

class AlgorithmusFactory:
    @staticmethod
    def create(algoTyp:str)-> Knuth | StepByStep | None:
        if algoTyp=="knuth":
            return Knuth()
        if algoTyp=="step_by_step":
            return StepByStep()
        else:
            return None