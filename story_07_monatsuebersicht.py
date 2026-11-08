from story_01_budgetzeitraum import geld


def monatsausgaben(ausgaben, monat):
    ergebnis = []
    for ausgabe in ausgaben:
        if ausgabe["monat"] == monat:
            ergebnis.append(ausgabe)
    return ergebnis


def ausgaben_anzeigen(ausgaben):
    gesamt = 0
    kategorien = {}
    for ausgabe in ausgaben:
        kategorie = ausgabe["kategorie"]
        betrag = ausgabe["betrag"]
        gesamt = gesamt + betrag
        if kategorie not in kategorien:
            kategorien[kategorie] = 0
        kategorien[kategorie] = kategorien[kategorie] + betrag

    print(f"Gesamtausgaben: {geld(gesamt)}")
    for kategorie in kategorien:
        print(f"{kategorie}: {geld(kategorien[kategorie])}")
