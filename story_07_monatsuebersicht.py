from story_01_budgetzeitraum import geld_formatieren


# Wählt die Buchungen für die Monatsübersicht aus.
def monatsausgaben_filtern(ausgaben: list[dict], monat: str) -> list[dict]:
    """
    Sammelt Ausgaben mit übereinstimmendem Monat ohne die Liste zu ändern.

    Args:
        ausgaben (list[dict]): Ausgaben mit Monat, Kategorie und Rappenbetrag.
        monat (str): Gültiger Monat im Format JJJJ-MM.

    Returns:
        list[dict]: Passende Ausgaben oder eine leere Liste.
    """
    ergebnis: list[dict] = []
    for ausgabe in ausgaben:
        if ausgabe["monat"] == monat:
            ergebnis.append(ausgabe)
    return ergebnis


# Zeigt die Ausgabenübersicht an.
def ausgaben_anzeigen(ausgaben: list[dict]) -> None:
    """
    Summiert Rappenbeträge insgesamt und je Kategorie und gibt CHF-Werte aus.

    Args:
        ausgaben (list[dict]): Ausgaben mit Monat, Kategorie und Rappenbetrag.

    Returns:
        None: Kein Rückgabewert.
    """
    gesamt: int = 0
    kategorien: dict[str, int] = {}
    for ausgabe in ausgaben:
        kategorie: str = ausgabe["kategorie"]
        betrag: int = ausgabe["betrag"]
        gesamt = gesamt + betrag
        if kategorie not in kategorien:
            kategorien[kategorie] = 0
        kategorien[kategorie] = kategorien[kategorie] + betrag

    print(f"Gesamtausgaben: {geld_formatieren(gesamt)}")
    for kategorie in kategorien:
        print(f"{kategorie}: {geld_formatieren(kategorien[kategorie])}")
