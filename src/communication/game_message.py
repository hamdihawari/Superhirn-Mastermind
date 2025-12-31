from dataclasses import dataclass
from .message_type import MessageType

# Einfache Datenklasse für Nachrichten im Kommunikationslayer
@dataclass
class GameMessage:
    """
    Datenobjekt für eine Spielnachricht.
    Enthält alle Informationen, die zwischen Spielteilnehmern ausgetauscht werden.
    """
    game_id: int  # ID des Spiels
    gamer_id: str  # ID des Spielers
    positions: int  # Anzahl richtiger Positionen
    colours: int  # Anzahl richtiger Farben
    value: str  # Gesendeter Wert (z. B. Spielzug)
    msg_type: MessageType  # Typ der Nachricht