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

    def __init__(self):
        super().__init__()
        self.message = {
                      "gameid" : 0,
                      "gamerid" : "",
                      "positions" : 0,
                      "colors" : 0,
                      "value" : ""}
    @responses.activate
    def starte(self, variante: Variante) -> bool:
        v = variante

        # Anzahl an Farben und Steckplätze in die Nachricht schreiben
        self.message["positions"] = v.steckplaetze
        self.message["colors"] = v.anzahlFarben

        # Nachricht erstes Mal verschicken und Antwort empfangen
        response = rq.post("http://141.45.34.161:5001/", json = self.message)
        response_status = response.status_code
        response_json = response.json()

        #gameid überschreiben
        self.message["gameid"] = response_json["gameid"]

        # wenn der Server geantwortet(200er code) hat
        # und die gameid richtig überschrieben wurde(ist am anfang 0)
        # wird true zurückgegeben sonst false
        if response_status == 200 and response_json["gameid"] != 0:
            return True
        else:
            return False

    def sendeVersuch(self, code: Code) -> Feedback:
        uebersetzter_code = ""
        # Farbencode in integer übersetzen
        for farbe in code.farben:
            uebersetzter_code += str(farbe.value)


        # übersetzten Farbencode in message schreiben
        self.message["value"] = uebersetzter_code


        # request mit übersetztem code schicken und Antwort emfpangen
        response = rq.post("http://141.45.34.161:5001/", json = self.message)
        response_json = response.json()

        #Antwort in feedback schreiben und dabei die integer in Farben umwandeln
        response_zahlencode = response_json["value"]
        schwarz = 0
        weiss = 0
        for z in response_zahlencode:
            if int(z) == 8:
                schwarz = schwarz + 1
            if int(z) == 7:
                weiss = weiss + 1

        feedback = Feedback(schwarz, weiss)


        return feedback






