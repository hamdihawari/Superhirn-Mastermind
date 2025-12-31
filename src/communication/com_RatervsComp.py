from .com_factory import ComFactory
from .com_tcp import ComTcp
from .json_serializer import JsonSerializer

class PlayerGuesserFactory(ComFactory):
    """
    Factory für Spieler = Rater gegen Server.
    """

    def __init__(self, server_address: str, server_port: int):
        super().__init__(serializer=JsonSerializer())
        self.server_address = server_address
        self.server_port = server_port

    def create(self):
        # erzeugt einen TCP-Port für Server-Kommunikation
        return ComTcp(self.server_address, self.server_port, self.serializer)