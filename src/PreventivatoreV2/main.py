from typing import List, Dict
import googleapiclient.discovery
from google.oauth2 import service_account

class GoogleDriveAPI:
    """Classe per le operazioni di basso livello su Google Drive"""
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
            'credentials.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        self.service = googleapiclient.discovery.build('sheets', 'v4', credentials=self.credentials)
        self.spreadsheet_id = "YOUR_SPREADSHEET_ID"
        self.sheet_name = "Ordini"

    def read_range(self, range_name: str):
        request = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f"{self.sheet_name}!{range_name}"
        )
        return request.execute()

    def write_range(self, range_name: str, values: List):
        request = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f"{self.sheet_name}!{range_name}",
            valueInputOption="RAW",
            body={"values": values}
        )
        return request.execute()

    def delete_row(self, row_index: int):
        request = self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "requests": [
                    {
                        "deleteDimension": {
                            "range": {
                                "sheetId": 0,
                                "dimension": "ROWS",
                                "startIndex": row_index,
                                "endIndex": row_index + 1
                            }
                        }
                    }
                ]
            }
        )
        return request.execute()

class OrdineExporter:
    """Facade per l'esportazione degli ordini"""
    def __init__(self):
        self._drive_api = GoogleDriveAPI()

    def _trova_riga_vuota(self) -> int:
        values = self._drive_api.read_range("A:A")
        return len(values.get('values', [])) + 1

    def _trova_riga_ordine(self, codice_ordine: str) -> int:
        values = self._drive_api.read_range("A:A")
        for i, row in enumerate(values.get('values', [])):
            if row[0] == codice_ordine:
                return i + 1
        return -1

    def _converti_ordine_in_riga(self, ordine: Dict) -> List:
        return [
            ordine['codice'],
            ordine['importo_base'],
            ordine['sconto'],
            ordine['totale']
        ]

    def aggiungi_ordine(self, ordine: Dict):
        """Aggiunge un nuovo ordine al foglio"""
        try:
            riga = self._trova_riga_vuota()
            dati = self._converti_ordine_in_riga(ordine)
            self._drive_api.write_range(f"A{riga}:D{riga}", [dati])
        except Exception as e:
            print(f"Errore nell'aggiunta dell'ordine: {e}")

    def modifica_ordine(self, ordine: Dict):
        """Modifica un ordine esistente"""
        try:
            riga = self._trova_riga_ordine(ordine['codice'])
            if riga > 0:
                dati = self._converti_ordine_in_riga(ordine)
                self._drive_api.write_range(f"A{riga}:D{riga}", [dati])
        except Exception as e:
            print(f"Errore nella modifica dell'ordine: {e}")

    def elimina_ordine(self, codice_ordine: str):
        """Elimina un ordine"""
        try:
            riga = self._trova_riga_ordine(codice_ordine)
            if riga > 0:
                self._drive_api.delete_row(riga - 1)
        except Exception as e:
            print(f"Errore nell'eliminazione dell'ordine: {e}")

# Esempio di utilizzo
def main():
    exporter = OrdineExporter()
    
    # Esempio di ordine
    ordine = {
        'codice': 'ORD001',
        'importo_base': 1000,
        'sconto': 0.1,
        'totale': 900
    }
    
    # Operazioni CRUD
    exporter.aggiungi_ordine(ordine)
    ordine['totale'] = 850
    exporter.modifica_ordine(ordine)
    exporter.elimina_ordine('ORD001')

if __name__ == "__main__":
    main()