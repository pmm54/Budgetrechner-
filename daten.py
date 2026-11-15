from pathlib import Path

DATENDATEI: Path = Path(__file__).with_name("budgetdaten.txt")


# Lädt Budget, Einnahmen, Ausgaben und Archiv aus der TXT-Datei.
def daten_laden() -> dict:
    """
    Lädt Budget, Einnahmen, Ausgaben und Archiv aus der TXT-Datei.

    Returns:
        dict: Budget, Einnahmen, Ausgaben und Archiv; ohne Datei leer.
    """
    daten: dict = {
        "budget": {},
        "ausgaben": [],
        "einnahmen": [],
        "archiv": {},
    }

    if not DATENDATEI.exists():
        return daten

    with open(DATENDATEI, "r", encoding="utf-8") as datei:
        for zeile in datei:
            # Die Kategorie steht am Ende und darf selbst ein | enthalten.
            teile: list[str] = zeile.rstrip("\n").split("|", 3)
            art: str = teile[0]
            monat: str = teile[1]

            if art == "BUDGET":
                daten["budget"] = {
                    "start": monat,
                    "dauer": int(teile[2]),
                    "betrag": int(teile[3]),
                }
            elif art == "ARCHIV":
                daten["archiv"][monat] = {
                    "budget": int(teile[2]),
                    "ausgaben": [],
                }
            else:
                eintrag: dict = {
                    "monat": monat,
                    "betrag": int(teile[2]),
                    "kategorie": teile[3],
                }
                if art == "AUSGABE":
                    daten["ausgaben"].append(eintrag)
                elif art == "EINNAHME":
                    daten["einnahmen"].append(eintrag)
                elif art == "ARCHIVAUSGABE":
                    daten["archiv"][monat]["ausgaben"].append(eintrag)

    return daten


# Speichert Budget, Einnahmen, Ausgaben und Archiv in der TXT-Datei.
def daten_speichern(daten: dict) -> None:
    """
    Speichert Budget, Einnahmen, Ausgaben und Archiv in der TXT-Datei.

    Args:
        daten (dict): Gemeinsame Programmdaten.

    Returns:
        None: Kein Rückgabewert.
    """
    with open(DATENDATEI, "w", encoding="utf-8") as datei:
        budget: dict = daten["budget"]
        if budget != {}:
            datei.write(
                f"BUDGET|{budget['start']}|{budget['dauer']}"
                f"|{budget['betrag']}\n"
            )

        for ausgabe in daten["ausgaben"]:
            datei.write(
                f"AUSGABE|{ausgabe['monat']}|{ausgabe['betrag']}"
                f"|{ausgabe['kategorie']}\n"
            )

        for einnahme in daten.get("einnahmen", []):
            datei.write(
                f"EINNAHME|{einnahme['monat']}|{einnahme['betrag']}"
                f"|{einnahme['kategorie']}\n"
            )

        for monat in daten["archiv"]:
            eintrag: dict = daten["archiv"][monat]
            datei.write(f"ARCHIV|{monat}|{eintrag['budget']}\n")
            for ausgabe in eintrag["ausgaben"]:
                datei.write(
                    f"ARCHIVAUSGABE|{monat}|{ausgabe['betrag']}"
                    f"|{ausgabe['kategorie']}\n"
                )
