from src.spiel.strategie.algoStrat import AlgorithmusStrategie
from src.spiel.strategie.player import Player


class HumanPlayer(Player):
    def __init__(self):
        pass



class ComputerPlayer(Player):
    def __init__(self,algo:AlgorithmusStrategie):
        self.algo=algo

