import requests
import pytest


@pytest.fixture
def startMessage():
    #message = GameMessage(0, "",4,  6, "")
    message = {"gameid": 14100827, "gamerid": "", "positions": 4, "colors": 6, "value": "2345"}
    return message



@pytest.fixture
def super_superhirn_message():
    message = {"gameid": 0, "gamerid": "", "positions": 5, "colors": 8, "value": ""}
    return message



def test_handshake_superhirn(startMessage):
    response = requests.post(
        "http://141.45.34.161:5001/", json = startMessage)

    print (response.status_code)
    print (response.json())


def test_handshake_super_superhirn(super_superhirn_message):
    response = requests.post("http://141.45.34.161:5001/", json = super_superhirn_message)

    print(response.status_code)
    print(response.json())







