from abc import ABC, abstractmethod

class Sacchetto(ABC):
    @abstractmethod
    def descrizione(self):
        pass


class SacchettoXYZ123(Sacchetto):
    def descrizione(self):
        return "Sacchetto compatibile con il modello XYZ123"


class SacchettoABC456(Sacchetto):
    def descrizione(self):
        return "Sacchetto compatibile con il modello ABC456"
