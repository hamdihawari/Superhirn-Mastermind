from enum import Enum

class MessageType(Enum):
    MOVE = "MOVE"
    RESULT = "RESULT"
    START = "START"
    ERROR = "ERROR"