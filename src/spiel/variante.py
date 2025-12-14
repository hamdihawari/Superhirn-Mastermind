from enum import Enum

from src.spiel.farbe import Farbe


class Variante(Enum):
    #anzahlFarben oder erlaubte Farben überflüssig?
    SUPER = (6,4,10,(Farbe.ROT, Farbe.GRUEN, Farbe.BLAU,Farbe.GELB,Farbe.ORANGE,Farbe.BRAUN))
    SUPERSUPER =(8,5,10,(Farbe.ROT, Farbe.GRUEN, Farbe.BLAU,Farbe.GELB,Farbe.ORANGE,Farbe.BRAUN,Farbe.WEISS,Farbe.SCHWARZ))

    def __init__(self, anzahlFarben, steckplaetze, maxVersuche, erlaubteFarben):
        self.anzahlFarben = anzahlFarben
        self.steckplaetze = steckplaetze
        self.maxVersuche = maxVersuche
        self.erlaubteFarben = erlaubteFarben