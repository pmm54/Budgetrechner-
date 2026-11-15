from pathlib import Path

DATENDATEI = Path(__file__).with_name("budgetdaten.txt")


def laden():
    daten = {
        "budget": {},
        "ausgaben": [],
        "archiv": {},
    }

    if not DATENDATEI.exists():
        return daten

    with open(DATENDATEI, "r", encoding="utf-8") as datei:
        for zeile in datei:
            # Die Kategorie steht am Ende und darf selbst ein | enthalten.
            teile = zeile.rstrip("\n").split("|", 3)
            art = teile[0]
            monat = teile[1]

            if art == "BUDGET":
                daten["budget"] = {
                    "start": monat,
                    "dauer": int(teile[2]),
                    "betrag": int(teile[3]),
                }
            elif art == "ARCHIV":
                daten["archiv"][monat] = {"budget": int(teile[2]), "ausgaben": []}
            else:
                ausgabe = {"monat": monat, "betrag": int(teile[2]), "kategorie": teile[3]}
                if art == "AUSGABE":
                    daten["ausgaben"].append(ausgabe)
                elif art == "ARCHIVAUSGABE":
                    daten["archiv"][monat]["ausgaben"].append(ausgabe)

    return daten


def speichern(daten):
    with open(DATENDATEI, "w", encoding="utf-8") as datei:
        budget = daten["budget"]
        if budget != {}:
            datei.write(f"BUDGET|{budget['start']}|{budget['dauer']}|{budget['betrag']}\n")

        for ausgabe in daten["ausgaben"]:
            datei.write(f"AUSGABE|{ausgabe['monat']}|{ausgabe['betrag']}|{ausgabe['kategorie']}\n")

        for monat in daten["archiv"]:
            eintrag = daten["archiv"][monat]
            datei.write(f"ARCHIV|{monat}|{eintrag['budget']}\n")
            for ausgabe in eintrag["ausgaben"]:
                datei.write(f"ARCHIVAUSGABE|{monat}|{ausgabe['betrag']}|{ausgabe['kategorie']}\n")
