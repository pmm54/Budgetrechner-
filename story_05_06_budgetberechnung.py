from story_01_budgetzeitraum import geld_formatieren


# Berechnet eine Monatssumme.
def monatssumme_berechnen(transaktionen: list[dict], monat: str) -> int:
    """
    Addiert nur Rappenbeträge mit passendem Monat; die Liste bleibt
    unverändert.

    Args:
        transaktionen (list[dict]): Einnahmen oder Ausgaben in Rappen.
        monat (str): Gültiger Monat im Format JJJJ-MM.

    Returns:
        int: Monatssumme in Rappen, ohne Einträge null.
    """
    summe: int = 0
    for eintrag in transaktionen:
        if eintrag["monat"] == monat:
            summe = summe + eintrag["betrag"]
    return summe


# Meldet eine Budgetüberschreitung.
def budgetwarnung_anzeigen(restbudget: int) -> None:
    """
    Gibt nur bei negativem Restbudget den positiven Fehlbetrag in CHF aus.

    Args:
        restbudget (int): Einnahmen minus Ausgaben in Rappen.

    Returns:
        None: Kein Rückgabewert.
    """
    if restbudget < 0:
        print(
            "Warnung: Die Ausgaben übersteigen die Einnahmen um "
            f"{geld_formatieren(-restbudget)}."
        )


# Zeigt das verfügbare Monatsbudget an.
def verfuegbares_budget_anzeigen(daten: dict, monat: str) -> None:
    """
    Subtrahiert aktuelle Monatsausgaben von Einnahmen und prüft die Warnung.

    Args:
        daten (dict): Gemeinsame Programmdaten.
        monat (str): Gültiger Monat im Format JJJJ-MM.

    Returns:
        None: Kein Rückgabewert.
    """
    einnahmen: int = monatssumme_berechnen(daten["einnahmen"], monat)
    ausgaben: int = monatssumme_berechnen(daten["ausgaben"], monat)
    restbudget: int = einnahmen - ausgaben
    print(f"Monat: {monat}")
    print(f"Einnahmen: {geld_formatieren(einnahmen)}")
    print(f"Ausgaben: {geld_formatieren(ausgaben)}")
    print(f"Verfügbares Budget: {geld_formatieren(restbudget)}")
    budgetwarnung_anzeigen(restbudget)
