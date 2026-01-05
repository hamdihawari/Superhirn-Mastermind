from enum import Enum

from src.spiel.spielCodes import Code
from src.spiel.variante import Variante

class Modus(Enum):
    M_C=1
    C_M=2
    C_C=3

class Sprache(Enum):
    DEUTSCH=1
    ENGLISH=2

class Spielparameter:
    def __init__(self,variante: Variante,modus: Modus,delay: int, sprache: Sprache, code: Code):
        self.variante = variante
        self.modus = modus
        self.delay = delay
        self.sprache = sprache
        self.code = code
