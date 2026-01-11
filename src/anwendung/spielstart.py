from abc import ABC, abstractmethod

from src.anwendung.spielengine import SpielEngine, EngineInterface
from src.anwendung.spielparameter import Spielparameter




class StarterInt(ABC):

    @abstractmethod
    def starteSpiel(self,param:Spielparameter) -> EngineInterface:
        pass



class Spielstarter(ABC):

    def starteSpiel(self,param:Spielparameter) -> SpielEngine:
        return SpielEngine(param)
