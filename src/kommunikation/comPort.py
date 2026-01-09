from abc import ABC, abstractmethod
from src.spiel.spielCodes import Code, Feedback
from src.spiel.variante import Variante
from src.spiel.farbe import Farbe
import requests as rq


class ComPort(ABC):
    """
    Abstrakte Basisklasse für alle Kommunikationsports.
    Definiert, wie Nachrichten gesendet und empfangen werden.
    """

    def __init__(self):
        pass


    @abstractmethod
    def starte(self, variante: Variante) -> bool:
        pass

    # Sendet eine Nachricht über den jeweiligen Kommunikationskanal
    @abstractmethod
    def sendeVersuch(self, code: Code) -> Feedback:
        pass


class ComJson(ComPort):

    def __init__(self, ):
        super().__init__()
        self.message = {
                      "gameid" : 0,
                      "gamerid" : "",
                      "positions" : 0,
                      "colors" : 0,
                      "value" : ""}

    def starte(self, variante: Variante) -> bool:
        v = variante

        self.message["positions"] = v.steckplaetze
        self.message["colors"] = v.anzahlFarben

        response = rq.post("http://141.45.34.161:5001/", json = self.message)
        response_status = response.status_code
        response_json = response.json()

        self.message["gameid"] = response_json["gameid"]

        if response_status == 200 and response_json["gameid"] != 0:
            return True
        else:
            return False

    def sendeVersuch(self, code: Code) -> Feedback:
        uebersetzter_code = ""
        # Farbencode in integer übersetzen
        for farbe in code.farben:
            uebersetzter_code += str(farbe.value)

        uebersetzter_code = int(uebersetzter_code)

        # übersetzten Farbencode in message schreiben
        self.message["value"] = uebersetzter_code

        # request mit übersetztem code schicken und Antwort emfpangen
        response = rq.post("http://141.45.34.161:5001/", json = self.message)
        response_json = response.json()

        #Antwort in feedback schreiben und dabei die integer in Farben umwandeln
        response_zahlencode = str(response_json["value"])
        feedback = []
        for z in response_zahlencode:
            feedback.append(Farbe(int(z))) # wie genau soll feedback dann aussehen?

        return feedback






