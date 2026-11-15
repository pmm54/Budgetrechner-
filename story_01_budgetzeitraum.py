from daten import speichern


def geld(rappen):
    franken = rappen // 100
    rest = rappen % 100
    return f"CHF {franken}.{rest:02d}"


def ist_ganzzahl(text):
    return text.isascii() and text.isdigit()


def monat_eingeben(aufforderung):
    monat = input(aufforderung + " (JJJJ-MM): ").strip()
    if len(monat) == 7 and monat[4] == "-":
        jahr = monat[:4]
        nummer = monat[5:]
        if ist_ganzzahl(jahr) and ist_ganzzahl(nummer):
            if int(jahr) >= 1 and 1 <= int(nummer) <= 12:
                return monat
    print("Bitte einen gültigen Monat eingeben, zum Beispiel 2026-09.")
    return ""


def monatsnummer(monat):
    # Fortlaufende Monatsnummer, damit Dezember und Januar aufeinanderfolgen.
    jahr = int(monat[:4])
    monat_im_jahr = int(monat[5:])
    return jahr * 12 + monat_im_jahr - 1


def monat_aus_nummer(nummer):
    jahr = nummer // 12
    monat_im_jahr = nummer % 12 + 1
    return f"{jahr:04d}-{monat_im_jahr:02d}"


def budget_erfassen(daten):
    start = monat_eingeben("Startmonat")
    if start == "":
        return

    eingabe = input("Anzahl Monate: ").strip()
    if not ist_ganzzahl(eingabe):
        print("Bitte eine positive ganze Anzahl Monate eingeben.")
        return
    eingabe = eingabe.lstrip("0")
    if eingabe == "":
        print("Bitte eine positive ganze Anzahl Monate eingeben.")
        return
    if len(eingabe) > 6:
        print("Der Endmonat liegt ausserhalb des gültigen Zeitraums.")
        return
    dauer = int(eingabe)
    ende = monatsnummer(start) + dauer - 1
    if ende > monatsnummer("9999-12"):
        print("Der Endmonat liegt ausserhalb des gültigen Zeitraums.")
        return

    eingabe = input("Gesamtbudget in CHF: ").strip()
    eingabe = eingabe.replace(",", ".")
    teile = eingabe.split(".")
    if len(teile) > 2 or not ist_ganzzahl(teile[0]):
        print("Bitte einen gültigen Betrag eingeben, zum Beispiel 2400.00.")
        return

    franken = teile[0].lstrip("0")
    if len(franken) > 12:
        print("Der Budgetbetrag ist zu gross.")
        return
    betrag = 0
    if franken != "":
        betrag = int(franken) * 100

    if len(teile) == 2:
        nachkomma = teile[1]
        if not ist_ganzzahl(nachkomma) or len(nachkomma) > 2:
            print("Bitte höchstens zwei Nachkommastellen eingeben.")
            return
        if len(nachkomma) == 1:
            nachkomma = nachkomma + "0"
        betrag = betrag + int(nachkomma)

    daten["budget"] = {"start": start, "dauer": dauer, "betrag": betrag}
    speichern(daten)
    print("Budgetzeitraum gespeichert.")


def budget_anzeigen(budget):
    if budget == {}:
        print("Es wurde noch kein Budget erfasst.")
        return
    ende = monatsnummer(budget["start"]) + budget["dauer"] - 1
    print(f"Startmonat: {budget['start']}")
    print(f"Endmonat: {monat_aus_nummer(ende)}")
    print(f"Gesamtbudget: {geld(budget['betrag'])}")
