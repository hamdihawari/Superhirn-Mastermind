from abc import ABC

from src.anwendung.spielparameter import Modus
from src.spiel.spielCodes import Code, Feedback
from src.spiel.variante import Variante


class ComPort(ABC):

    def starte(self,variante:Variante)->bool:
        pass

    def sendeVersuch(self,code:Code)->Feedback:
        pass

