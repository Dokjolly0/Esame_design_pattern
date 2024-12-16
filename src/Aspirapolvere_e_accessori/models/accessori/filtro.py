from abc import ABC, abstractmethod

class Filtro(ABC):
    @abstractmethod
    def descrizione(self):
        pass


class FiltroXYZ123(Filtro):
    def descrizione(self):
        return "Filtro compatibile con il modello XYZ123"


class FiltroABC456(Filtro):
    def descrizione(self):
        return "Filtro compatibile con il modello ABC456"
