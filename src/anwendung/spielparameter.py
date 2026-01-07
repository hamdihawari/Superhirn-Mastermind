from enum import Enum

from src.anwendung.modus import Modus
from src.spiel.spielCodes import Code
from src.spiel.variante import Variante
from src.ui.sprache import Sprache


class Spielparameter:
    def __init__(self,variante: Variante,modus: Modus,algorithmus:str,delay: int, sprache: Sprache, code: Code):
        self.variante = variante
        self.modus = modus
        self.algorithmus = algorithmus
        self.delay = delay
        self.sprache = sprache
        self.code = code
