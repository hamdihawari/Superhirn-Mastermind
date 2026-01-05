from abc import ABC, abstractmethod
from .com_port import ComPort
from .game_message import GameMessage
from .json_serializer import JsonSerializer


class ComFactory(ABC):
    """
    Abstrakte Factory für die Erzeugung von ComPort-Objekten.
    """

    def __init__(self, serializer: JsonSerializer, message: GameMessage):
        self.serializer = serializer
        self.message = message

    @abstractmethod
    def createCom(self):
        pass