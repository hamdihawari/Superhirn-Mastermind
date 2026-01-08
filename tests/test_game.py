import pytest

from src.anwendung.modus import Modus
from src.anwendung.spielparameter import Spielparameter
from src.spiel.variante import Variante
from src.spiel.spielCodes import Code
from src.spiel.farbe import Farbe
from src.spiel.game import Game
from unittest.mock import patch


@pytest.fixture
def geheim_code():
    return Code([Farbe.ORANGE, Farbe.GELB, Farbe.GELB, Farbe.ROT])

@pytest.fixture
def geheim_code2():
    return Code([Farbe.ROT, Farbe.GELB, Farbe.GELB, Farbe.ORANGE,Farbe.SCHWARZ])


@pytest.fixture
def parameter():
    return Spielparameter(Variante.SUPER, Modus.C_M,"knuth",1,None)

@pytest.fixture
def parameter2():
    return Spielparameter(Variante.SUPERSUPER, Modus.C_M,"knuth",1,None)


@pytest.fixture
def game(parameter,geheim_code):
    # Mocke die Methode während der Game-Initialisierung
    with patch('src.spiel.strategie.playerType.ComputerPlayer.generiereGeheimeCode',
               return_value=geheim_code):
        return Game(parameter)


@pytest.fixture
def game2(parameter2,geheim_code2):
    # Mocke die Methode während der Game-Initialisierung
    with patch('src.spiel.strategie.playerType.ComputerPlayer.generiereGeheimeCode',
               return_value=geheim_code2):
        return Game(parameter2)


def test_game_startzustand(game):
    assert game.runden == []
    assert game.istFertig() is False


def test_feedback_alle_schwarz(game):
    rate = Code([Farbe.ORANGE, Farbe.GELB, Farbe.GELB, Farbe.ROT])

    feedback = game.fuehreRateversuchDurch(rate)

    assert feedback.schwarz == 4
    assert feedback.weiss == 0

def test_feedback_alle_schwarz2(game2):
    rate = Code([Farbe.ROT, Farbe.GELB, Farbe.GELB, Farbe.ORANGE,Farbe.SCHWARZ])
    feedback = game2.fuehreRateversuchDurch(rate)

    assert feedback.schwarz == 5
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



