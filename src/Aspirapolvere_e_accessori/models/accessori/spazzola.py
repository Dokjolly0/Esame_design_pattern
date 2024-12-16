from abc import ABC, abstractmethod

class Spazzola(ABC):
    @abstractmethod
    def descrizione(self):
        pass


class SpazzolaXYZ123(Spazzola):
    def descrizione(self):
        return "Spazzola compatibile con il modello XYZ123"


class SpazzolaABC456(Spazzola):
    def descrizione(self):
        return "Spazzola compatibile con il modello ABC456"
