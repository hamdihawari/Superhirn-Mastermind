import json
from .game_message import GameMessage

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
            "colors": message.colors,
            "value": message.value,

        })

    # Wandelt einen JSON-String zurück in eine GameMessage
    def deserialize(self, data: str) -> GameMessage:
        obj = json.loads(data)
        return GameMessage(
            game_id=obj["gameId"],
            gamer_id=obj["gamerId"],
            positions=obj["positions"],
            colors=obj["colors"],
            value=obj["value"],

        )