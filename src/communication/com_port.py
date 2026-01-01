from abc import ABC, abstractmethod
from .game_message import GameMessage

class ComPort(ABC):
    """
    Abstrakte Basisklasse für alle Kommunikationsports.
    Definiert, wie Nachrichten gesendet und empfangen werden.
    """


    @abstractmethod
    def start(self):
        pass

    # Sendet eine Nachricht über den jeweiligen Kommunikationskanal
    @abstractmethod
    def send(self, message: GameMessage):
        pass

    # Empfängt eine Nachricht über den jeweiligen Kommunikationskanal
    @abstractmethod
    def receive(self) -> GameMessage:
        pass