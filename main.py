while True:
    print ("1:Ausgaben Erfassen", "2:Einnahmen erfassen","3:Budgetzeitraum festelgen","4:Suchen","5:Kategorien Verwalten",sep="\n")

    Menu_Choice = (input("Choose your next Step:"))

    if Menu_Choice == "1":
        print("Ausgaben erfassen")
    elif Menu_Choice == "2":
        print ("Einnahmen erfassen")
    elif Menu_Choice == "3":
        print ("Budgetzeitraum festlegen")
    elif Menu_Choice == "4":
        print ("Suchen")
    elif Menu_Choice == "5":
        while True:
            print("\n1: Kategorie hinzufügen","2: Kategorie löschen","3: Kategorien anzeigen","4: Zurück zum Hauptmenü",sep="\n")
            menu_choice_kategorien = (input("\nWählen Sie einen der Schritte zwischen 1-3:"))
            if menu_choice_kategorien == "1":
                from Katergorien import kategorie_hinzufügen
                from Katergorien import kategorien_set
                kategorie_input_hinzufügen = (input("\nGeben Sie den Namen der Kategorie ein, welche Sie hinzufügen möchten:")).upper()
                kategorie_hinzufügen(kategorie_input_hinzufügen)
            elif menu_choice_kategorien == "2":
                from Katergorien import kategorien_löschen
                from Katergorien import kategorien_set
                kategorie_input_löschen = (input("\nGeben Sie den Namen der Kategorie ein, welche Sie löschen möchten:")).upper()
                kategorien_löschen(kategorie_input_löschen)
            elif menu_choice_kategorien =="3":
                from Katergorien import kategorien_set
                if len(kategorien_set) == 0:
                    print("\nKeine Kategorien vorhaden")
                else:
                    print("\nKategorien\n")
                    for kategorie in kategorien_set:
                        print(kategorie)
            elif menu_choice_kategorien == "4":
                break
    else:
        print("\nUngültige Eingabe, bitte geben Sie eine Zahl zwischen 1-5 ein,\n")