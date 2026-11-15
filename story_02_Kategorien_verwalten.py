kategorien_set = set()

def kategorie_hinzufügen(name_kategorie):
    if name_kategorie in kategorien_set:
        print("\nKategorie " + name_kategorie + " besteht bereits")
    else:
        kategorien_set.add(name_kategorie)
        print ("\nKategorie " + name_kategorie + " wurde hinzugefügt")


def kategorien_löschen(name_kategorie_löschen):
    while True:
        if name_kategorie_löschen in kategorien_set:
            bestätigung_löschen = (input("Definitiv löschen? Ja oder Nein ?")).upper()
            if bestätigung_löschen == "JA":
                kategorien_set.remove(name_kategorie_löschen)
                print("\nKategorie wurde gelöscht")
                break
            elif bestätigung_löschen == "NEIN":
                print("\nKategorie wurde nicht gelöscht")
                break
            else:
                print("\nBitte antworten Sie mit Ja oder Nein\n")
                continue
        else:
            print("\nKategorie wurde nicht gefunden")
            break
                



