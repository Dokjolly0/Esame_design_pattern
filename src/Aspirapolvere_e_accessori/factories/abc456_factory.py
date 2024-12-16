from factories.accessorio_factory import AccessorioFactory
from models.accessori.spazzola import SpazzolaABC456
from models.accessori.filtro import FiltroABC456
from models.accessori.sacchetto import SacchettoABC456

class ABC456Factory(AccessorioFactory):
    # Implementazione del metodo crea_spazzola per creare un'istanza di SpazzolaABC456
    def crea_spazzola(self):
        return SpazzolaABC456()

    # Implementazione del metodo crea_filtro per creare un'istanza di FiltroABC456
    def crea_filtro(self):
        return FiltroABC456()

    # Implementazione del metodo crea_sacchetto per creare un'istanza di SacchettoABC456
    def crea_sacchetto(self):
        return SacchettoABC456()
