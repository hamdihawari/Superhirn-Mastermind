from abc import ABC, abstractmethod
from src.spiel.spielCodes import Code, Feedback
from src.anwendung.spielparameter import Modus
from src.spiel.variante import Variante
import requests as rq


class ComPort(ABC):
    """
    Abstrakte Basisklasse für alle Kommunikationsports.
    Definiert, wie Nachrichten gesendet und empfangen werden.
    """

    def __init__(self, ComFactory):
        self.factory = ComFactory


    @abstractmethod
    def start(self, modus: Modus, variante: Variante):
        pass

    # Sendet eine Nachricht über den jeweiligen Kommunikationskanal
    @abstractmethod
    def send(self, code: Code) -> Feedback:
        pass


class ComJson(ComPort):
    pass


