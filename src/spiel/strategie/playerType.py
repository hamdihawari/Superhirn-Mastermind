from typing import List

from src.spiel.spielCodes import Code
from src.spiel.spielrunde import SpielRunde
from src.spiel.strategie.player import Player
from src.spiel.variante import Variante


class HumanPlayer(Player):

    def __init__(self):
        pass

    def generiereGeheimeCode(self, variante: Variante) -> Code:
        pass

    def generiereVersuch(self, runden: List['SpielRunde']) -> Code:
        pass




class ComputerPlayer(Player):

    def __init__(self,algo:str):
        self.algo=algo

    def generiereVersuch(self, runden: list[SpielRunde]) -> Code:
        pass


    def generiereGeheimeCode(self, variante: Variante) -> Code:
        pass



