from abc import ABC, abstractmethod
from .com_port import ComPort

class ComFactory(ABC):
    """
    Abstrakte Factory für die Erzeugung von ComPort-Objekten.
    """

    def __init__(self, serializer):
        self.serializer = serializer

    @abstractmethod
    def create(self) -> ComPort:
        pass