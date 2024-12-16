class Aspirapolvere:
    def __init__(self, nome, factory):
        self.nome = nome
        self.factory = factory
        self.spazzola = self.factory.crea_spazzola()
        self.filtro = self.factory.crea_filtro()
        self.sacchetto = self.factory.crea_sacchetto()

    def mostra_dettagli(self):
        dettagli = f"Aspirapolvere: {self.nome}\n"
        dettagli += f"  - {self.spazzola.descrizione()}\n"
        dettagli += f"  - {self.filtro.descrizione()}\n"
        dettagli += f"  - {self.sacchetto.descrizione()}\n"
        return dettagli
