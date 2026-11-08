from datetime import date

from daten import speichern
from story_01_budgetzeitraum import geld, monat_eingeben, monatsnummer
from story_07_monatsuebersicht import ausgaben_anzeigen, monatsausgaben


def monat_archivieren(daten, monat):
    heute = date.today()
    aktueller_monat = f"{heute.year:04d}-{heute.month:02d}"
    if monat >= aktueller_monat:
        print("Nur vergangene Monate können archiviert werden.")
        return
    if monat in daten["archiv"]:
        print("Dieser Monat ist bereits archiviert.")
        return

    budget = daten["budget"]
    if budget == {}:
        print("Erfasse zuerst einen Budgetzeitraum.")
        return
    startnummer = monatsnummer(budget["start"])
    monatsabstand = monatsnummer(monat) - startnummer
    dauer = budget["dauer"]
    if monatsabstand < 0 or monatsabstand >= dauer:
        print("Für diesen Monat ist kein Budget vorhanden.")
        return

    ausgaben = monatsausgaben(daten["ausgaben"], monat)
    if ausgaben == []:
        print("Für diesen Monat sind keine Ausgaben vorhanden.")
        return

    # Übrige Rappen werden einzeln auf die ersten Monate verteilt.
    gesamtbudget = budget["betrag"]
    monatsbudget = gesamtbudget // dauer
    rest = gesamtbudget % dauer
    if monatsabstand < rest:
        monatsbudget = monatsbudget + 1

    # Spätere Änderungen an einer Buchung dürfen das Archiv nicht ändern.
    archivierte_ausgaben = []
    for ausgabe in ausgaben:
        archivierte_ausgaben.append(ausgabe.copy())

    daten["archiv"][monat] = {"budget": monatsbudget, "ausgaben": archivierte_ausgaben}
    speichern(daten)
    print(f"{monat} wurde archiviert.")


def archiv_anzeigen(archiv):
    if archiv == {}:
        print("Es sind noch keine Monate archiviert.")
        return

    print("Archivierte Monate:")
    for monat in archiv:
        print(monat)
    monat = monat_eingeben("Archivmonat")
    if monat == "":
        return
    if monat not in archiv:
        print("Dieser Monat ist im Archiv nicht vorhanden.")
        return

    eintrag = archiv[monat]
    print(f"Archiv {monat}")
    print(f"Monatsbudget: {geld(eintrag['budget'])}")
    ausgaben_anzeigen(eintrag["ausgaben"])
    for ausgabe in eintrag["ausgaben"]:
        print(f"  {ausgabe['kategorie']} – {geld(ausgabe['betrag'])}")
