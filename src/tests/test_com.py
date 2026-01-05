import requests
import pytest
from src.communication.json_serializer import JsonSerializer
from src.communication.game_message import GameMessage

@pytest.fixture
def startMessage()-> GameMessage:
    message = GameMessage(0, "",4,  6, "")
    return message

@pytest.fixture
def jsonMessage():
    message = GameMessage(0,"", 4, 6, "")
    abc = JsonSerializer()
    json = abc.serialize(message)
    return json


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

def test_server_message(jsonMessage):
    response = requests.post(
        "http://localhost:5000/game", json = jsonMessage)


    print (response.status_code)
    print (response.json())






