from abc import ABC, abstractmethod
from typing import Dict

# Strategy Interface
class StrategiaPreventivo(ABC):
    @abstractmethod
    def calcola_preventivo(self, dati: Dict) -> float:
        pass

# Concrete Strategies
class PreventivoBase(StrategiaPreventivo):
    def calcola_preventivo(self, dati: Dict) -> float:
        base = dati.get('importo_base', 0)
        return base * 1.22  # IVA 22%

class PreventivoSconto(StrategiaPreventivo):
    def calcola_preventivo(self, dati: Dict) -> float:
        base = dati.get('importo_base', 0)
        sconto = dati.get('sconto', 0)
        return (base * (1 - sconto)) * 1.22

class PreventivoPremium(StrategiaPreventivo):
    def calcola_preventivo(self, dati: Dict) -> float:
        base = dati.get('importo_base', 0)
        extra = dati.get('servizi_extra', 0)
        return (base + extra) * 1.22

# Context
class Preventivatore:
    def __init__(self, strategia: StrategiaPreventivo):
        self._strategia = strategia

    def set_strategia(self, strategia: StrategiaPreventivo):
        self._strategia = strategia

    def genera_preventivo(self, dati: Dict) -> float:
        return self._strategia.calcola_preventivo(dati)

# Output di esempio
if __name__ == "__main__":
    dati_base = {"importo_base": 1000}
    dati_sconto = {"importo_base": 1000, "sconto": 0.1}
    dati_premium = {"importo_base": 1000, "servizi_extra": 200}

    preventivatore = Preventivatore(PreventivoBase())

    print("Preventivo Base:", preventivatore.genera_preventivo(dati_base))

    preventivatore.set_strategia(PreventivoSconto())
    print("Preventivo con Sconto:", preventivatore.genera_preventivo(dati_sconto))

    preventivatore.set_strategia(PreventivoPremium())
    print("Preventivo Premium:", preventivatore.genera_preventivo(dati_premium))