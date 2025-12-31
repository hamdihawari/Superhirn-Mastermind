import json
from .game_message import GameMessage, MessageType

class JsonSerializer:
    """
    Serializer für den Kommunikationslayer.
    Wandelt GameMessage-Objekte in JSON um und wieder zurück.
    """

    # Wandelt eine GameMessage in einen JSON-String um
    def serialize(self, message: GameMessage) -> str:
        return json.dumps({
            "gameId": message.game_id,
            "gamerId": message.gamer_id,
            "positions": message.positions,
            "colours": message.colours,
            "value": message.value,
            "type": message.msg_type.value
        })

    # Wandelt einen JSON-String zurück in eine GameMessage
    def deserialize(self, data: str) -> GameMessage:
        obj = json.loads(data)
        return GameMessage(
            game_id=obj["gameId"],
            gamer_id=obj["gamerId"],
            positions=obj["positions"],
            colours=obj["colours"],
            value=obj["value"],
            msg_type=MessageType(obj["type"])
        )