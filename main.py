# Define functie betekent dat ik een functie creeer
def startspel():
    # Initialiseer alles. init per persoon een voorwerp heeft dat hij of zij gaat uitspreken bij het spel
    persoonVoorwerpDict = {
        "Yigit": "Voetbal",
        "Jurgen": "Laptop",
        "Luc": "Telefoon",
        "Loes": "NAS"
    }
    meegenomenVoorwerpen = []  # Lege lijst om de meegenomen voorwerpen in op te slaan
    draaiende_personen = list(persoonVoorwerpDict.keys())  # Lijst van mensen die rondjes draaien

    # Laat de toeschouwer weten dat het spel is gestart
    print("Spel is gestart!")
    print("\n")

    totaal_woorden = 0  # Voor het bijhouden van het aantal woorden dat wordt gesproken
    
    # Loop door elke deelnemer en hun voorwerp in de dictionary
    for persoon, voorwerp in persoonVoorwerpDict.items():
        meegenomenVoorwerpen.append(voorwerp)  # Voeg voorwerp toe aan de lijst

        # Print wie nog steeds rondjes draaien
        print("De volgende mensen draaien rondjes: "+ ', '.join(draaiende_personen))
        
        # De huidige persoon doet de activiteit
        itemsOpgenoemd = ", ".join(meegenomenVoorwerpen)  # Combineer alle meegenomen voorwerpen
        zin = persoon + " zegt: 'Ik ga op vakantie en neem mee: " + itemsOpgenoemd + "'"
        print(zin)
        
        # Tel de woorden in deze zin
        totaal_woorden += len(zin.split())
        
        # De persoon gaat zitten
        draaiende_personen.remove(persoon)  # Verwijder de persoon uit de lijst van draaiende mensen
        print(f"{persoon} gaat zitten.")
    
    # Overzicht van deelnemers en hun bijbehorende voorwerpen weergeven
    print("\nOverzicht van deelnemers en hun eigen voorwerp:")
    for persoon, voorwerp in persoonVoorwerpDict.items():
        print(persoon + " heeft " + voorwerp + " meegenomen.")
    
    # Laatste bericht dat ze aan het zingen zijn
    print("\nDe deelnemers drinken iets terwijl ze gezellig het Nederlandse volkslied zingen!")
    
    # Toon het totaal aantal gesproken woorden
    print("Totaal aantal woorden dat er gesproken is totdat ze gingen zingen: " + str(totaal_woorden) + ".")

# Roep de functie aan om het spel te starten
startspel()

# Programmeer deze casus. Zorg dat de output van het programma gelijk is aan wat jij zou horen als je als toeschouwer in dezelfde ruimte zou zijn.

# Daarnaast toon je op het eind een overzicht in de console met

#     de namen van de deelnemers + hun eigen voorwerp.
#     het totaal aantal woorden dat er gesproken is totdat ze gingen zingen

# Geef onderaan je code in een blok commentaar antwoord op de volgende vragen, indien van toepassing:

# Als je geen functies hebt gebruikt, leg dan uit waarom niet.
# Als je geen list hebt gebruikt, leg dan uit waarom niet.
## Als je geen tuple hebt gebruikt, leg dan uit waarom niet.
# Als je geen dictionary hebt gebruikt, leg dan uit waarom niet.
# Als je geen for hebt gebruikt, leg dan uit waarom niet.
## Als je geen while hebt gebruikt, leg dan uit waarom niet


# Geen tuple want ik gebruik een dictionary deze behoud voorwerpen vast bij elke persoon dus standaard heeft een persoon dezelfde voorwerp vast voor deze casus dus heb geen aparte tuple nodig die standaard voorwerpen vast heeft en ook niet voor personen omdat dictionary deze vervangt
# Geen while loop want waarom wel? Voor mijn Casus is dit niet nodig, de for loop was veel beter omdat ik door elke persoon heen moet loopen en als iedereen is geweest dan stopt de loop al een while loop stopt pas als die een waarde is langs gekomen eigenlijk kan het dus wel maar vond for loop prima voor deze casus.