from abc import ABC, abstractmethod

from src.anwendung.spielengine import SpielEngine, EngineInt
from src.anwendung.spielparameter import Spielparameter




class StarterInt(ABC):

    @abstractmethod
    def starteSpiel(self,param:Spielparameter) ->EngineInt:
        pass

    @abstractmethod
    def starteParallel(self,param:Spielparameter,param2:Spielparameter) -> list[EngineInt]:
        pass


class Spielstarter(ABC):

    def starteSpiel(param:Spielparameter) -> SpielEngine:
        return SpielEngine(param)

    def starteParallel(param:Spielparameter,param2:Spielparameter) -> list[SpielEngine]:
        return [SpielEngine(param),SpielEngine(param2)]

