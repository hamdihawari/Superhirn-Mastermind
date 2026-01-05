from dataclasses import dataclass


# Einfache Datenklasse für Nachrichten im Kommunikationslayer
@dataclass
class GameMessage:
    """
    Datenobjekt für eine Spielnachricht.
    Enthält alle Informationen, die zwischen Spielteilnehmern ausgetauscht werden.
    """

    game_id : int
    gamer_id : str
    positions : int
    colors : int
    value : str



