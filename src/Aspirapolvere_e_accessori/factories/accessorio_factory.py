from abc import ABC, abstractmethod

class AccessorioFactory(ABC):
    # Definizione dell'interfaccia per la factory degli accessori   
    @abstractmethod
    def crea_spazzola(self):
        pass

    # Definizione dell'interfaccia per la factory degli accessori   
    @abstractmethod
    def crea_filtro(self):
        pass

    # Definizione dell'interfaccia per la factory degli accessori   
    @abstractmethod
    def crea_sacchetto(self):
        pass
