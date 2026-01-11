from typing import Tuple, Iterable
from src.spiel.farbe import Farbe


class Code:

    def __init__(self, farben: Iterable[Farbe]):
        self._farben = tuple(farben)

    @property
    def farben(self) -> Tuple[Farbe, ...]:
        return self._farben

    @property
    def laenge(self) -> int:
        return len(self._farben)

    @farben.setter
    def farben(self, value: Iterable[Farbe]):
        self._farben = tuple(value)


class Feedback:
    """
    Args:
        schwarz(int): richtige Farbe, richtige Posi
        weiss(int): richtige Farbe, falsche Posi
    """

    def __init__(self, schwarz: int, weiss: int):
        self.schwarz = schwarz
        self.weiss = weiss

    @property
    def black(self) -> int:
        return self.schwarz

    @property
    def white(self) -> int:
        return self.weiss