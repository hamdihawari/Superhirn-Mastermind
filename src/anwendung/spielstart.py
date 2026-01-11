from abc import ABC, abstractmethod

from src.anwendung.spielengine import SpielEngine, EngineInt
from src.anwendung.spielparameter import Spielparameter




class StarterInt(ABC):

    @abstractmethod
    def starteSpiel(self,param:Spielparameter) ->EngineInt:
        pass



class Spielstarter(ABC):

    def starteSpiel(self,param:Spielparameter) -> SpielEngine:
        return SpielEngine(param)
