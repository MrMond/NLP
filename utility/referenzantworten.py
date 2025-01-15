import web_scraper
import openpyxl

vector_store = web_scraper.receive_vector_store()


# Funktion zur Eingabe von Antworten zu Fragen
def frage_und_antwort_sammeln(fragen_liste):
    antworten = []
    for frage in fragen_liste:
        print(frage)
        antwort = vector_store.similarity_search(frage)
        print(antwort)
        antworten.append(antwort)
    return antworten

# Funktion zum Speichern der Fragen und Antworten in eine Excel-Datei
def speichern_in_excel(dateiname, fragen, antworten):
    # Erstelle ein neues Workbook
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Fragen und Antworten"

    # Schreibe Überschriften
    sheet["A1"] = "Frage"
    sheet["B1"] = "Antwort"

    # Schreibe die Fragen und Antworten in die Tabelle
    for i, (frage, antwort) in enumerate(zip(fragen, antworten), start=2):
        sheet[f"A{i}"] = frage
        sheet[f"B{i}"] = str(antwort)

    # Speichere die Datei
    wb.save(dateiname)
    print(f"Daten erfolgreich in {dateiname} gespeichert!")

# Hauptprogramm
if __name__ == "__main__":

    fragen_liste = [
        "How is Lebron James performing?",
        "Should I add Lebron James to my team?",
        "What is the recent performance of Lebron James?",
        "How is Nikola Jokic performing?",
        "Should I add Nikola Jokic to my team?",
        "What is the recent performance of Nikola Jokic?",
        "How is Goga Bitadze performing?",
        "Should I add Goga Bitadze to my team?",
        "What is the recent performance of Goga Bitadze",
        "How are the Los Angeles Lakers performing?",
        "How are the Orlando Magic performing?"
    ]

    print("Bitte beantworte die folgenden Fragen:")
    
    # Fragen und Antworten sammeln
    antworten_liste = frage_und_antwort_sammeln(fragen_liste)

    # Excel-Dateiname definieren
    excel_dateiname = "fragen_und_antworten.xlsx"

    # Daten in Excel speichern
    speichern_in_excel(excel_dateiname, fragen_liste, antworten_liste)



