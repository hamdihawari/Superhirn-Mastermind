from enum import Enum

class Modus(Enum):
    """Einfache Enum für die Spielmodus-Auswahl (ohne UI-Logik)"""
    M_C = "Mensch-Computer"
    C_M = "Computer-Mensch"
    C_C = "Computer-Computer"
    C_M_ONLINE = "Computer-Mensch(On)"
    C_C_ONLINE = "Computer-Computer(On)"