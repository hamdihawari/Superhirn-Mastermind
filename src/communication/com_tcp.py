import socket
from .com_port import ComPort
from .game_message import GameMessage
from .json_serializer import JsonSerializer

class ComTcp(ComPort):
    """
    TCP-Implementierung eines ComPorts für Server-Kommunikation.
    """

    def __init__(self, server_address: str, server_port: int, serializer: JsonSerializer):
        self.server_address = server_address
        self.server_port = server_port
        self.serializer = serializer
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_address, self.server_port))

    def send(self, message: GameMessage):
        data = self.serializer.serialize(message)
        self.sock.sendall(data.encode('utf-8'))

    def receive(self) -> GameMessage:
        received = self.sock.recv(4096).decode('utf-8')
        return self.serializer.deserialize(received)

    def close(self):
        self.sock.close()