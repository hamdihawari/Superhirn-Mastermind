import pytest
import pytest_mock
import responses
from src.kommunikation.comPort import ComJson
from src.spiel.variante import Variante
from src.spiel.spielCodes import Code
from src.spiel.spielCodes import Feedback
from src.spiel.farbe import Farbe

@responses.activate
def test_start_superhirn_true():
    resp = responses.Response(
        method="POST",
        url = "http://141.45.34.161:5001/",
        json = {"gameid": 123, "gamerid" : "", "positions": 4, "colors": 6, "value": ""}
    )

    responses.add(resp)

    test_objekt = ComJson()

    b = test_objekt.starte(variante= Variante.SUPER)
    positionen = test_objekt.message["positions"]
    anzahl_farben = test_objekt.message["colors"]

    assert b
    assert positionen == 4
    assert anzahl_farben == 6


@responses.activate
def test_start_superhirn_false():
    resp = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json={"gameid": 0, "gamerid": "", "positions": 4, "colors": 6, "value": ""}
    )

    responses.add(resp)

    test_objekt = ComJson()

    b = test_objekt.starte(variante= Variante.SUPER)
    positionen = test_objekt.message["positions"]
    anzahl_farben = test_objekt.message["colors"]

    assert not b
    assert positionen == 4
    assert anzahl_farben == 6

@responses.activate
def test_start_super_superhirn_true():
    resp = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json= {"gameid": 123456, "gamerid": "", "positions": 5, "colors": 8, "value": ""}
    )
    responses.add(resp)

    test_objekt = ComJson()
    b = test_objekt.starte(variante= Variante.SUPERSUPER)
    positionen = test_objekt.message["positions"]
    anzahl_farben = test_objekt.message["colors"]


    assert b
    assert positionen == 5
    assert anzahl_farben == 8

@responses.activate
def test_start_super_superhirn_false():
    resp = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json={"gameid": 0, "gamerid": "", "positions": 5, "colors": 8, "value": ""}
    )

    responses.add(resp)

    test_objekt = ComJson()
    b = test_objekt.starte(variante= Variante.SUPERSUPER)
    positionen = test_objekt.message["positions"]
    anzahl_farben = test_objekt.message["colors"]

    assert not b
    assert positionen == 5
    assert anzahl_farben == 8

@responses.activate
def test_sendeversuch_superhirn():
    resp1 = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json = {"gameid": 12, "gamerid": "", "positions": 4, "colors": 6, "value": ""}
    )
    resp2 = responses.Response(
        method = "POST",
        url = "http://141.45.34.161:5001/",
        json = {"gameid": 12, "gamerid": "", "positions": 4, "colors": 6, "value": "8777"}
    )
    responses.add(resp1)
    responses.add(resp2)

    farben_liste = [Farbe.ROT, Farbe.BLAU, Farbe.GELB, Farbe.ORANGE]
    code = Code(farben= farben_liste)


    test_objekt = ComJson()

    b = test_objekt.starte(variante= Variante.SUPER)
    feedback = test_objekt.sendeVersuch(code)


    assert test_objekt.message["value"] == "1435"
    assert b
    assert feedback.schwarz == 1
    assert feedback.weiss == 3

@responses.activate
def test_sendeversuch_super_superhirn():
    resp1 = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json={"gameid": 12, "gamerid": "", "positions": 5, "colors": 8, "value": ""}
    )
    resp2 = responses.Response(
        method="POST",
        url="http://141.45.34.161:5001/",
        json={"gameid": 12, "gamerid": "", "positions": 5, "colors": 8, "value": "88887"}
    )
    responses.add(resp1)
    responses.add(resp2)

    farben_liste = [Farbe.ROT, Farbe.BLAU, Farbe.GELB, Farbe.ORANGE,Farbe.BRAUN]
    code = Code(farben=farben_liste)

    test_objekt = ComJson()

    b = test_objekt.starte(variante=Variante.SUPERSUPER)
    feedback = test_objekt.sendeVersuch(code)

    assert test_objekt.message["value"] == "14356"
    assert b
    assert feedback.schwarz == 4
    assert feedback.weiss == 1





