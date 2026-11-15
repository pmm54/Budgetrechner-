from datetime import date, datetime

from daten import daten_speichern
from story_01_budgetzeitraum import (
    geld_formatieren,
    monat_eingeben,
    monatsnummer_berechnen,
)
from story_07_monatsuebersicht import ausgaben_anzeigen, monatsausgaben_filtern


# Bewahrt einen vergangenen Monatsstand auf.
def monat_archivieren(daten: dict, monat: str) -> None:
    """
    Prüft den Monat und speichert Monatsbudget und kopierte Ausgaben im Archiv.

    Args:
        daten (dict): Gemeinsame Programmdaten.
        monat (str): Gültiger Monat im Format JJJJ-MM.

    Returns:
        None: Kein Rückgabewert.
    """
    heute: date = date.today()
    aktueller_monat: date = heute.replace(day=1)
    archivmonat: date = datetime.strptime(monat, "%Y-%m").date()
    if archivmonat >= aktueller_monat:
        print("Nur vergangene Monate können archiviert werden.")
        return
    if monat in daten["archiv"]:
        print("Dieser Monat ist bereits archiviert.")
        return

    budget: dict = daten["budget"]
    if not budget:
        print("Erfasse zuerst einen Budgetzeitraum.")
        return
    startnummer: int = monatsnummer_berechnen(budget["start"])
    monatsabstand: int = monatsnummer_berechnen(monat) - startnummer
    dauer: int = budget["dauer"]
    if monatsabstand < 0 or monatsabstand >= dauer:
        print("Für diesen Monat ist kein Budget vorhanden.")
        return

    ausgaben: list[dict] = monatsausgaben_filtern(daten["ausgaben"], monat)
    if not ausgaben:
        print("Für diesen Monat sind keine Ausgaben vorhanden.")
        return

    # Übrige Rappen werden einzeln auf die ersten Monate verteilt.
    gesamtbudget: int = budget["betrag"]
    monatsbudget: int = gesamtbudget // dauer
    rest: int = gesamtbudget % dauer
    if monatsabstand < rest:
        monatsbudget = monatsbudget + 1

    # Spätere Änderungen an einer Buchung dürfen das Archiv nicht ändern.
    archivierte_ausgaben: list[dict] = []
    for ausgabe in ausgaben:
        archivierte_ausgaben.append(ausgabe.copy())

    daten["archiv"][monat] = {
        "budget": monatsbudget,
        "ausgaben": archivierte_ausgaben,
    }
    daten_speichern(daten)
    print(f"{monat} wurde archiviert.")


# Öffnet einen gespeicherten Monatsstand.
def archiv_anzeigen(archiv: dict) -> None:
    """
    Listet Archivmonate und gibt Budget und Ausgaben der gewählten Kopie aus.

    Args:
        archiv (dict): Gespeicherte Monatsstände.

    Returns:
        None: Kein Rückgabewert.
    """
    if not archiv:
        print("Es sind noch keine Monate archiviert.")
        return

    print("Archivierte Monate:")
    for monat in archiv:
        print(monat)
    monat: str = monat_eingeben("Archivmonat")
    if monat == "":
        return
    if monat not in archiv:
        print("Dieser Monat ist im Archiv nicht vorhanden.")
        return

    eintrag: dict = archiv[monat]
    print(f"Archiv {monat}")
    print(f"Monatsbudget: {geld_formatieren(eintrag['budget'])}")
    ausgaben_anzeigen(eintrag["ausgaben"])
    for ausgabe in eintrag["ausgaben"]:
        print(
            f"  {ausgabe['kategorie']} – "
            f"{geld_formatieren(ausgabe['betrag'])}"
        )
