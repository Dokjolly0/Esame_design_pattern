from factories.xyz123_factory import XYZ123Factory
from factories.abc456_factory import ABC456Factory
from models.aspirapolvere import Aspirapolvere

def main():
    # Creazione degli aspirapolvere con le relative factory
    aspirapolvere_xyz = Aspirapolvere("SuperClean XYZ123", XYZ123Factory())
    aspirapolvere_abc = Aspirapolvere("PowerVac ABC456", ABC456Factory())

    # Mostra i dettagli di ciascun aspirapolvere
    print(aspirapolvere_xyz.mostra_dettagli())
    print(aspirapolvere_abc.mostra_dettagli())

if __name__ == "__main__":
    # Esecuzione del programma
    main()
