from enum import Enum

class Sprache(Enum):
    DEUTSCH = {
        "description": "Deutsch",
        "ueberschrift": "Übersicht",
        "variante_auswaehlen": "Variante auswählen:",
        "modus_auswaehlen": "Modus auswählen:",
        "sprache_auswaehlen": "Sprache auswählen:",
        "bestaetigen": "Bestätigen",
        "einstellungen": "Einstellungen",
        "farbauswahl": "Farbauswahl:",
        "algorithmus_auswaehlen": "Algorithmus auswählen:",
        "zeitverzoegerung": "Zeitverzögerung der Maschine in Sekunden:",
        "zurueck": "Zurück",
        "starten": "Spiel starten"
    }

    ENGLISCH = {
        "description": "English",
        "ueberschrift": "Overview",
        "variante_auswaehlen": "Select variant:",
        "modus_auswaehlen": "Select mode:",
        "sprache_auswaehlen": "Select language:",
        "bestaetigen": "Confirm",
        "einstellungen": "Settings",
        "farbauswahl": "Color selection:",
        "algorithmus_auswaehlen": "Select algorithm:",
        "zeitverzoegerung": "Machine delay in seconds:",
        "zurueck": "Back",
        "starten": "Game start"
    }

    def __init__(self, translations):
        self._translations = translations

    @property
    def description(self):
        return self._translations["description"]

    @property
    def ueberschrift(self):
        return self._translations["ueberschrift"]

    @property
    def variante_auswaehlen(self):
        return self._translations["variante_auswaehlen"]

    @property
    def modus_auswaehlen(self):
        return self._translations["modus_auswaehlen"]

    @property
    def sprache_auswaehlen(self):
        return self._translations["sprache_auswaehlen"]

    @property
    def bestaetigen(self):
        return self._translations["bestaetigen"]

    @property
    def codierer(self):
        return self._translations["codierer"]

    @property
    def rater(self):
        return self._translations["rater"]

    @property
    def zuschauer(self):
        return self._translations["zuschauer"]

    @property
    def einstellungen(self):
        return self._translations["einstellungen"]

    @property
    def farbauswahl(self):
        return self._translations["farbauswahl"]

    @property
    def algorithmus_auswaehlen(self):
        return self._translations["algorithmus_auswaehlen"]

    @property
    def zeitverzoegerung(self):
        return self._translations["zeitverzoegerung"]

    @property
    def zurueck(self):
        return self._translations["zurueck"]
    @property
    def starten(self):
        return self._translations["starten"]
