from daten import daten_speichern
from story_01_budgetzeitraum import (
    betrag_eingeben,
    geld_formatieren,
    ist_nichtnegative_ganzzahl,
    monat_eingeben,
)


# Fragt die Angaben einer Buchung ab.
def transaktion_eingeben() -> dict:
    """
    Prüft Monat, nichtleere Kategorie und Betrag vor dem Aufbau des Eintrags.

    Returns:
        dict: Monat, Kategorie und Rappenbetrag; bei Fehlern leer.
    """
    monat: str = monat_eingeben("Buchungsmonat")
    if monat == "":
        return {}
    kategorie: str = input("Kategorie: ").strip()
    if kategorie == "":
        print("Bitte eine Kategorie eingeben.")
        return {}
    betrag: int = betrag_eingeben("Betrag")
    if betrag < 0:
        return {}
    return {"monat": monat, "kategorie": kategorie, "betrag": betrag}


# Lässt eine vorhandene Buchung auswählen.
def transaktion_auswaehlen(transaktionen: list[dict]) -> int:
    """
    Zeigt nummerierte Einträge und übersetzt eine gültige Nummer in den Index.

    Args:
        transaktionen (list[dict]): Einnahmen oder Ausgaben.

    Returns:
        int: Listenindex oder -1 bei leerer Liste oder ungültiger Auswahl.
    """
    if not transaktionen:
        print("Es sind noch keine Einträge vorhanden.")
        return -1
    for nummer, eintrag in enumerate(transaktionen, start=1):
        print(
            f"{nummer}: {eintrag['monat']} | {eintrag['kategorie']} | "
            f"{geld_formatieren(eintrag['betrag'])}"
        )
    eingabe: str = input("Nummer: ").strip()
    if ist_nichtnegative_ganzzahl(eingabe) and len(eingabe) <= 12:
        nummer: int = int(eingabe)
        if 1 <= nummer <= len(transaktionen):
            return nummer - 1
    print("Bitte eine Nummer aus der Liste wählen.")
    return -1


# Erfasst eine neue Buchung.
def transaktion_hinzufuegen(daten: dict, art: str) -> None:
    """
    Hängt einen gültigen Eintrag an daten[art] an und speichert die TXT-Datei.

    Args:
        daten (dict): Gemeinsame Programmdaten.
        art (str): Listenschlüssel einnahmen oder ausgaben.

    Returns:
        None: Kein Rückgabewert.
    """
    eintrag: dict = transaktion_eingeben()
    if not eintrag:
        return
    daten[art].append(eintrag)
    daten_speichern(daten)
    print("Eintrag gespeichert.")


# Ändert eine vorhandene Buchung.
def transaktion_bearbeiten(daten: dict, art: str) -> None:
    """
    Ersetzt den gewählten Listeneintrag erst nach gültiger vollständiger
    Eingabe.

    Args:
        daten (dict): Gemeinsame Programmdaten.
        art (str): Listenschlüssel einnahmen oder ausgaben.

    Returns:
        None: Kein Rückgabewert.
    """
    index: int = transaktion_auswaehlen(daten[art])
    if index < 0:
        return
    eintrag: dict = transaktion_eingeben()
    if not eintrag:
        return
    daten[art][index] = eintrag
    daten_speichern(daten)
    print("Eintrag geändert.")


# Entfernt eine vorhandene Buchung.
def transaktion_loeschen(daten: dict, art: str) -> None:
    """
    Löscht den ausgewählten Listenindex aus daten[art] und speichert die Datei.

    Args:
        daten (dict): Gemeinsame Programmdaten.
        art (str): Listenschlüssel einnahmen oder ausgaben.

    Returns:
        None: Kein Rückgabewert.
    """
    index: int = transaktion_auswaehlen(daten[art])
    if index < 0:
        return
    del daten[art][index]
    daten_speichern(daten)
    print("Eintrag gelöscht.")


# Öffnet die Buchungsverwaltung.
def transaktionen_verwalten(daten: dict) -> None:
    """
    Wählt Einnahmen oder Ausgaben und ruft die gewählte Bearbeitungsaktion auf.

    Args:
        daten (dict): Gemeinsame Programmdaten.

    Returns:
        None: Kein Rückgabewert.
    """
    while True:
        print("\n1 Eintrag hinzufügen")
        print("2 Eintrag bearbeiten")
        print("3 Eintrag löschen")
        print("0 Zurück")
        auswahl: str = input("Auswahl: ").strip()
        if auswahl == "0":
            return
        if auswahl not in ("1", "2", "3"):
            print("Bitte eine Zahl von 0 bis 3 wählen.")
            continue
        eingabe: str = input("1 Einnahme / 2 Ausgabe: ").strip()
        if eingabe == "1":
            art: str = "einnahmen"
        elif eingabe == "2":
            art = "ausgaben"
        else:
            print("Bitte 1 oder 2 wählen.")
            continue
        if auswahl == "1":
            transaktion_hinzufuegen(daten, art)
        elif auswahl == "2":
            transaktion_bearbeiten(daten, art)
        else:
            transaktion_loeschen(daten, art)
