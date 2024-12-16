from factories.accessorio_factory import AccessorioFactory
from models.accessori.spazzola import SpazzolaXYZ123
from models.accessori.filtro import FiltroXYZ123
from models.accessori.sacchetto import SacchettoXYZ123

class XYZ123Factory(AccessorioFactory):
    # Implementazione del metodo crea_spazzola per creare un'istanza di SpazzolaXYZ123
    def crea_spazzola(self):
        return SpazzolaXYZ123()

    # Implementazione del metodo crea_filtro per creare un'istanza di FiltroXYZ123  
    def crea_filtro(self):
        return FiltroXYZ123()

    # Implementazione del metodo crea_sacchetto per creare un'istanza di SacchettoXYZ123    
    def crea_sacchetto(self):
        return SacchettoXYZ123()
