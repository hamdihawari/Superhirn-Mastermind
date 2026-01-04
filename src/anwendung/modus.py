from enum import Enum

class Modus(Enum):
    # Modus: Mensch-Codierer (M-C)
    M_C = {
        "show_farbe": True,      # Farbauswahl anzeigen
        "show_algorithmus": True,  # Algorithmus anzeigen
        "show_zeit": True,       # Zeitverzögerung anzeigen
        "description": "(M-C)"
    }

    # Modus: Computer-Mensch (C-M, Rater)
    C_M = {
        "show_farbe": False,     # Farbauswahl ausblenden
        "show_algorithmus": False,  # Algorithmus ausblenden
        "show_zeit": True,       # Nur Zeit anzeigen
        "description": "(C-M)"
    }

    # Modus: Computer-Computer (C-C, Zuschauer)
    C_C = {
        "show_farbe": False,     # Alles ausblenden
        "show_algorithmus": False,
        "show_zeit": True,
        "description": "(C-C)"
    }

    def __init__(self, config):
        self._config = config  # Speichert die Konfiguration (Dict)

    @property
    def show_farbe(self):
        return self._config["show_farbe"]

    @property
    def show_algorithmus(self):
        return self._config["show_algorithmus"]

    @property
    def show_zeit(self):
        return self._config["show_zeit"]

    @property
    def description(self):
        return self._config["description"]