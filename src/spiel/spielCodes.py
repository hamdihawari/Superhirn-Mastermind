from typing import Tuple, Iterable
from src.spiel.farbe import Farbe


class Code:

    def __init__(self, farben: Iterable[Farbe]):
        self.farben = tuple(farben)

    @property
    def farben(self):
        return self._farben

    @property
    def laenge(self):
        return len(self._farben)



class Feedback:

    def __init__(self, black:int,white:int):
        self.black=black
        self.white=white


    @property
    def black(self):
        return self.black

    @property
    def white(self):
        return self.white
