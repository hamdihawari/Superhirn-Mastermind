import requests
import pytest
from src.communication.json_serializer import JsonSerializer
from src.communication.game_message import GameMessage

@pytest.fixture
def startMessage()-> GameMessage:
    #message = GameMessage(0, "",4,  6, "")
    message = {"gameid": 14100827, "gamerid": "", "positions": 4, "colors": 6, "value": "2345"}
    return message

@pytest.fixture
def jsonMessage():
    message = GameMessage(0,"", 4, 6, "")
    abc = JsonSerializer()
    json = abc.serialize(message)
    return json

@pytest.fixture
def super_superhirn_message():
    message = GameMessage(0, "", 5, 8, "")
    return message


def test_jsonSerializer(startMessage, jsonMessage):
    abc = JsonSerializer()
    json = abc.serialize(startMessage)
    assert json == jsonMessage

def test_jsonDeserializer(jsonMessage, startMessage):
    abc = JsonSerializer()
    gameMessage = abc.deserialize(jsonMessage)
    print (gameMessage)
    print (jsonMessage)
    assert gameMessage == startMessage

def test_handshake_superhirn(startMessage):
    response = requests.post(
        "http://141.45.34.161:5001/", json = startMessage)


    print (response.status_code)
    print (response.json())


def test_handshake_super_superhirn(super_superhirn_message):
    response = requests.post("http://141.45.34.161:5001/", json = super_superhirn_message)

    print(response.status_code)
    print(response.json())







