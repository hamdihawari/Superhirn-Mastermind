import pytest

from src.spiel.strategie.player import Player
from src.spiel.variante import Variante
from src.spiel.spielCodes import Code
from src.spiel.farbe import Farbe
from src.spiel.game import Game
from unittest.mock import Mock


@pytest.fixture
def geheim_code():
    return Code([Farbe.ORANGE, Farbe.GELB, Farbe.GELB, Farbe.ROT])


@pytest.fixture
def codierer():
    return Mock(spec=Player)

@pytest.fixture
def rater():
    return Mock(spec=Player)



@pytest.fixture
def game(geheim_code, codierer, rater):
    return Game(
        codierer=codierer,
        rater=rater,
        variante=Variante.SUPER,
        secret_code=geheim_code
    )


def test_game_startzustand(game):
    assert game.runden == []
    assert game.istFertig() is False


def test_feedback_alle_schwarz(game):
    rate = Code([Farbe.ORANGE, Farbe.GELB, Farbe.GELB, Farbe.ROT])

    feedback = game.fuehreRateversuchDurch(rate)

    assert feedback.schwarz == 4
    assert feedback.weiss == 0


def test_feedback_alle_weiss(game):
    rate = Code([Farbe.GELB, Farbe.ROT, Farbe.ORANGE, Farbe.GELB])

    feedback = game.fuehreRateversuchDurch(rate)

    assert feedback.schwarz == 0
    assert feedback.weiss == 4


def test_spielende_bei_erfolg(game):
    rate = Code([Farbe.ORANGE, Farbe.GELB, Farbe.GELB, Farbe.ROT])

    game.fuehreRateversuchDurch(rate)

    assert game.istFertig() is True
    assert len(game.runden) == 1
    assert game.runden[0].erfolgreich is True


def test_gemischtes_feedback(game):
    # Erwartung: 2 schwarz (ORANGE an Position 0), 1 weiß (ROT und GELB falsche Position)
    rate = Code([Farbe.ORANGE, Farbe.ROT, Farbe.GELB, Farbe.BLAU])

    feedback = game.fuehreRateversuchDurch(rate)

    assert feedback.schwarz == 2
    assert feedback.weiss == 1


def test_maximale_versuche_erreicht(game):
    max_versuche = game.variante.maxVersuche

    # Führe max_versuche fehlerhafte Rateversuche durch
    for _ in range(max_versuche):
        falscher_rate = Code([Farbe.BLAU, Farbe.BLAU, Farbe.BLAU, Farbe.BLAU])
        game.fuehreRateversuchDurch(falscher_rate)

    assert game.istFertig() is True
    assert len(game.runden) == max_versuche
    assert all(not runde.erfolgreich for runde in game.runden)



