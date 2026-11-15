buchungen = []

while True:
    print("\nBudgetrechner")
    print("1. Einnahme erfassen")
    print("2. Ausgabe erfassen")
    print("3. Buchungen anzeigen")
    print("4. Buchung bearbeiten")
    print("5. Buchung löschen")
    print("6. Programm beenden")

    auswahl = input("Deine Auswahl: ")

    if auswahl == "1":
        kategorie = input("Kategorie der Einnahme: ")
        while True:
            try:
                betrag = float(input("Betrag in CHF: "))
                if betrag > 0:
                    break
                else:
                    print("Bitte einen Betrag grösser als 0 eingeben.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

        einnahme = {
            "typ": "Einnahme",
            "kategorie": kategorie,
            "betrag": betrag
        }

        buchungen.append(einnahme)
        print("Einnahme erfolgreich erfasst!")
    elif auswahl == "2":
        kategorie = input("Kategorie der Ausgabe: ")
        while True:
            try:
                betrag = float(input("Betrag in CHF: "))
                if betrag > 0:
                    break
                else:
                    print("Bitte einen Betrag grösser als 0 eingeben.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

        ausgabe = {
            "typ": "Ausgabe",
            "kategorie": kategorie,
            "betrag": betrag
        }

        buchungen.append(ausgabe)
        print("Ausgabe erfolgreich erfasst!")
    elif auswahl == "3":
        print("Aktuelle Buchungen:")
        print(buchungen)


    elif auswahl == "4":
        print("Aktuelle Buchungen:")

        for nummer, buchung in enumerate(buchungen):
            print(nummer, buchung)

        if len(buchungen) > 0:
            while True:
                try:
                    nummer = int(input("Welche Buchung bearbeiten? "))
                    break
                except ValueError:
                    print("Bitte eine gültige Buchungsnummer eingeben.")

            if 0 <= nummer < len(buchungen):
                neue_kategorie = input("Neue Kategorie: ")
                while True:
                    try:
                        neuer_betrag = float(input("Neuer Betrag in CHF: "))
                        if neuer_betrag > 0:
                            break
                        else:
                            print("Bitte einen Betrag grösser als 0 eingeben.")
                    except ValueError:
                        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")

                buchungen[nummer]["kategorie"] = neue_kategorie
                buchungen[nummer]["betrag"] = neuer_betrag

                print("Buchung erfolgreich geändert!")
            else:
                print("Ungültige Buchungsnummer!")
        else:
            print("Keine Buchungen vorhanden.")


    elif auswahl == "5":
        print("Aktuelle Buchungen:")

        for nummer, buchung in enumerate(buchungen):
            print(nummer, buchung)

        if len(buchungen) > 0:
            nummer = int(input("Welche Buchung löschen? "))

            if 0 <= nummer < len(buchungen):
                buchungen.pop(nummer)
                print("Buchung erfolgreich gelöscht!")
            else:
                print("Ungültige Buchungsnummer!")
        else:
            print("Keine Buchungen vorhanden.")

    elif auswahl == "6":
        print("Programm beendet.")
        break

    else:
        print("Diese Funktion ergänzen wir später.")
