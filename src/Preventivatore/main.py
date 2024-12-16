from abc import ABC, abstractmethod
from typing import List

class ComponentePreventivo(ABC):
    def __init__(self, nome: str, sconto: float = 0):
        self.nome = nome
        self.sconto = sconto

    @abstractmethod
    def get_prezzo_base(self) -> float:
        pass

    @abstractmethod
    def get_prezzo_scontato(self) -> float:
        pass

    def applica_sconto(self, prezzo: float) -> float:
        return prezzo * (1 - self.sconto)

class ElementoBase(ComponentePreventivo):
    def __init__(self, nome: str, prezzo: float, sconto: float = 0):
        super().__init__(nome, sconto)
        self.prezzo = prezzo

    def get_prezzo_base(self) -> float:
        return self.prezzo

    def get_prezzo_scontato(self) -> float:
        return self.applica_sconto(self.prezzo)

class Sezione(ComponentePreventivo):
    def __init__(self, nome: str, sconto: float = 0):
        super().__init__(nome, sconto)
        self.componenti: List[ComponentePreventivo] = []

    def aggiungi_componente(self, componente: ComponentePreventivo):
        self.componenti.append(componente)

    def get_prezzo_base(self) -> float:
        return sum(comp.get_prezzo_base() for comp in self.componenti)

    def get_prezzo_scontato(self) -> float:
        somma_scontata = sum(comp.get_prezzo_scontato() for comp in self.componenti)
        return self.applica_sconto(somma_scontata)

def main():
    # Creazione della struttura del preventivo
    preventivo = Sezione("Preventivo Completo")

    # Sezione macchina base e accessori
    sez_macchina = Sezione("Macchina base e accessori", 0.05)
    
    conf_base = Sezione("Configurazione base")
    conf_base.aggiungi_componente(ElementoBase("Macchina", 20000))
    conf_base.aggiungi_componente(ElementoBase("Accessorio1", 500))
    conf_base.aggiungi_componente(ElementoBase("Accessorio2", 300))
    conf_base.aggiungi_componente(ElementoBase("Accessorio3", 450))
    
    acc_extra = Sezione("Accessori extra", 0.1)
    acc_extra.aggiungi_componente(ElementoBase("Accessorio4", 800))
    acc_extra.aggiungi_componente(ElementoBase("Accessorio5", 600))
    
    sez_macchina.aggiungi_componente(conf_base)
    sez_macchina.aggiungi_componente(acc_extra)

    # Sezione servizi aggiuntivi
    servizi = Sezione("Servizi aggiuntivi")
    garanzie = Sezione("Garanzie aggiuntive", 0.15)
    garanzie.aggiungi_componente(ElementoBase("Garanzia estesa", 1000))
    garanzie.aggiungi_componente(ElementoBase("Riparazione internazionale", 500))
    garanzie.aggiungi_componente(ElementoBase("Assistenza telefono h24", 300))
    servizi.aggiungi_componente(garanzie)

    # Sezione trasporto
    trasporto = Sezione("Trasporto", 0.05)
    trasporto.aggiungi_componente(ElementoBase("Corriere1", 200))
    trasporto.aggiungi_componente(ElementoBase("Imballaggio2", 150))

    # Aggiunta delle sezioni principali al preventivo
    preventivo.aggiungi_componente(sez_macchina)
    preventivo.aggiungi_componente(servizi)
    preventivo.aggiungi_componente(trasporto)

    # Stampa risultati
    print(f"Prezzo base totale: €{preventivo.get_prezzo_base():.2f}")
    print(f"Prezzo scontato totale: €{preventivo.get_prezzo_scontato():.2f}")

if __name__ == "__main__":
    main()