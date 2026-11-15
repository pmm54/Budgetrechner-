from datetime import date, datetime

from daten import daten_speichern


# Bereitet Geldbeträge für die Anzeige auf.
def geld_formatieren(rappen: int) -> str:
    """
    Zerlegt ganze Rappen in Vorzeichen, Franken und zwei Rappenstellen.

    Args:
        rappen (int): Geldbetrag in Rappen.

    Returns:
        str: Betrag im Format CHF Franken.Rappen.
    """
    vorzeichen: str = ""
    if rappen < 0:
        vorzeichen = "-"
    franken: int = abs(rappen) // 100
    rest: int = abs(rappen) % 100
    return f"CHF {vorzeichen}{franken}.{rest:02d}"


# Prüft eine Ganzzahleingabe.
def ist_nichtnegative_ganzzahl(text: str) -> bool:
    """
    Akzeptiert ausschliesslich nichtleere Texte aus ASCII-Ziffern.

    Args:
        text (str): Zu prüfender Text.

    Returns:
        bool: True bei mindestens einer ASCII-Ziffer, sonst False.
    """
    return text.isascii() and text.isdigit()


# Fragt einen gültigen Monat ab.
def monat_eingeben(aufforderung: str) -> str:
    """
    Prüft die Konsoleneingabe mit datetime und verlangt das Format JJJJ-MM.

    Args:
        aufforderung (str): Beschriftung der Eingabe.

    Returns:
        str: Gültiger Monat JJJJ-MM oder leerer Text bei Fehlern.
    """
    monat: str = input(aufforderung + " (JJJJ-MM): ").strip()
    try:
        datum: datetime = datetime.strptime(monat, "%Y-%m")
        if len(monat) == 7 and monat.isascii():
            return f"{datum.year:04d}-{datum.month:02d}"
    except ValueError:
        pass
    print("Bitte einen gültigen Monat eingeben, zum Beispiel 2026-09.")
    return ""


# Ermöglicht Berechnungen über Jahresgrenzen.
def monatsnummer_berechnen(monat: str) -> int:
    """
    Berechnet aus JJJJ-MM eine fortlaufende Nummer mit zwölf Monaten je Jahr.

    Args:
        monat (str): Gültiger Monat im Format JJJJ-MM.

    Returns:
        int: Jahr mal zwölf plus Monatsnummer minus eins.
    """
    # Fortlaufende Monatsnummer, damit Dezember und Januar aufeinanderfolgen.
    datum: datetime = datetime.strptime(monat, "%Y-%m")
    jahr: int = datum.year
    monat_im_jahr: int = datum.month
    return jahr * 12 + monat_im_jahr - 1


# Bereitet eine Monatsnummer für die Anzeige auf.
def monat_aus_monatsnummer(nummer: int) -> str:
    """
    Ermittelt Jahr und Monat durch Division und formatiert sie als JJJJ-MM.

    Args:
        nummer (int): Fortlaufende Monatsnummer.

    Returns:
        str: Monat im Format JJJJ-MM.
    """
    jahr: int = nummer // 12
    monat_im_jahr: int = nummer % 12 + 1
    datum: date = date(jahr, monat_im_jahr, 1)
    return f"{datum.year:04d}-{datum.month:02d}"


# Fragt einen Geldbetrag ab.
def betrag_eingeben(aufforderung: str) -> int:
    """
    Prüft CHF-Text mit Punkt oder Komma und rechnet ganzzahlig in Rappen um.

    Args:
        aufforderung (str): Beschriftung der Betragseingabe.

    Returns:
        int: Betrag in Rappen oder -1 bei ungültiger Eingabe.
    """
    eingabe: str = input(aufforderung + " in CHF: ").strip()
    eingabe = eingabe.replace(",", ".")
    teile: list[str] = eingabe.split(".")
    if len(teile) > 2 or not ist_nichtnegative_ganzzahl(teile[0]):
        print("Bitte einen gültigen Betrag eingeben, zum Beispiel 2400.00.")
        return -1

    franken: str = teile[0].lstrip("0")
    if len(franken) > 12:
        print("Der Betrag ist zu gross.")
        return -1
    betrag: int = 0
    if franken != "":
        betrag = int(franken) * 100

    if len(teile) == 2:
        nachkomma: str = teile[1]
        if not ist_nichtnegative_ganzzahl(nachkomma) or len(nachkomma) > 2:
            print("Bitte höchstens zwei Nachkommastellen eingeben.")
            return -1
        if len(nachkomma) == 1:
            nachkomma = nachkomma + "0"
        betrag = betrag + int(nachkomma)

    return betrag


# Erfasst den Budgetzeitraum.
def budget_erfassen(daten: dict) -> None:
    """
    Prüft Start, positive Dauer und Gesamtbetrag und speichert das Budget.

    Args:
        daten (dict): Gemeinsame Programmdaten.

    Returns:
        None: Kein Rückgabewert.
    """
    start: str = monat_eingeben("Startmonat")
    if start == "":
        return

    eingabe: str = input("Anzahl Monate: ").strip()
    if not ist_nichtnegative_ganzzahl(eingabe):
        print("Bitte eine positive ganze Anzahl Monate eingeben.")
        return
    eingabe = eingabe.lstrip("0")
    if eingabe == "":
        print("Bitte eine positive ganze Anzahl Monate eingeben.")
        return
    if len(eingabe) > 6:
        print("Der Endmonat liegt ausserhalb des gültigen Zeitraums.")
        return
    dauer: int = int(eingabe)
    ende: int = monatsnummer_berechnen(start) + dauer - 1
    if ende > monatsnummer_berechnen(date.max.strftime("%Y-%m")):
        print("Der Endmonat liegt ausserhalb des gültigen Zeitraums.")
        return

    betrag: int = betrag_eingeben("Gesamtbudget")
    if betrag < 0:
        return

    daten["budget"] = {"start": start, "dauer": dauer, "betrag": betrag}
    daten_speichern(daten)
    print("Budgetzeitraum gespeichert.")


# Zeigt das erfasste Budget an.
def budget_anzeigen(budget: dict) -> None:
    """
    Ermittelt den Endmonat aus Start und Dauer und gibt den Gesamtbetrag aus.

    Args:
        budget (dict): Budget mit Startmonat, Dauer und Betrag in Rappen.

    Returns:
        None: Kein Rückgabewert.
    """
    if not budget:
        print("Es wurde noch kein Budget erfasst.")
        return
    ende: int = monatsnummer_berechnen(budget["start"]) + budget["dauer"] - 1
    print(f"Startmonat: {budget['start']}")
    print(f"Endmonat: {monat_aus_monatsnummer(ende)}")
    print(f"Gesamtbudget: {geld_formatieren(budget['betrag'])}")
