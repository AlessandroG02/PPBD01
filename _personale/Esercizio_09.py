"""Esercizio - Nuovi Mercati
Requisiti: liste, insiemi, if, for

Abbiamo qualche milione da investire nell'apertura di una nuova attività commerciale. Prima di tutto però ci serve sapere quali negozi non sono disponibili a Trento in maniera da evitare di aprire l'ennesimo negozio di abbigliamento casual (E rischiare di andare in perdita!)

INPUT:

categorie: insieme di tutte le categorie possibile
competitor: lista di competitor con dati (nome_competitor, insieme_categorie_merci)
Scrivi del codice che

Stampa le categorie che non sono vendute da nessun competitor
Calcola per ogni categoria, da quanti competitor è venduta
Esempio - dati:

categorie = {a, b, c, d, e, f}
competitor = [("pippo", {a, c, e}), ("pluto", {c, d, e})]
il tuo codice deve stampare:

"Le categorie disponibili sono: {b, f}"
Categorie vendute da competitor:

[(a, 1), (b, 0), (c, 2), (d, 1), (e, 2), (f,0)]

# INPUT (NON modificare)
categorie = {"Ferramenta", "Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Cosmetici", "Pesce", "Alcolici", "Forniture Elettriche", "Telefonia"}
competitor = [
        ("GenerStore", {"Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Pesce", "Alcolici"}),
        ("MomentiElettrizzanti", {"Abbigliamento sportivo", "Videogames", "Gioielleria", "Alcolici", "Forniture Elettriche"}),
        ("TuttoEDiPiù", {"Videogames", "Gioielleria", "Pesce", "Alcolici", "Forniture Elettriche"}),
        ("ProfumoDiBuono", {"Pesce", "Alcolici", "Forniture Elettriche"}),
        ("PessimeCombo", {"Alcolici", "Telefonia"}),
]

# scrivi qui
    """
categorie = {"Ferramenta", "Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Cosmetici", "Pesce", "Alcolici", "Forniture Elettriche", "Telefonia"}
competitor = [
        ("GenerStore", {"Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Pesce", "Alcolici"}),
        ("MomentiElettrizzanti", {"Abbigliamento sportivo", "Videogames", "Gioielleria", "Alcolici", "Forniture Elettriche"}),
        ("TuttoEDiPiù", {"Videogames", "Gioielleria", "Pesce", "Alcolici", "Forniture Elettriche"}),
        ("ProfumoDiBuono", {"Pesce", "Alcolici", "Forniture Elettriche"}),
        ("PessimeCombo", {"Alcolici", "Telefonia"}),
]

# creo un insieme vuoto x le categorie vendute dai competitor
categorie_vendute = set()

# creiamo un dizionario vuoto x contare quante volte una categoria e` venduta
vendite_categorie = {}

# per ogni competitor
for nome, categorie_merce in competitor:
    # aggiungiamo le categorie vendute all`insieme delle categorie vendute
    categorie_vendute |= categorie_merce
    # per ogni categoria venduta dal competitor
    for categoria in categorie_merce:
        # se la categoria non e` ancora presente nel dizionario delle vendite
        if categoria not in vendite_categorie:
            # la aggiungo con valore 1
            vendite_categorie[categoria] = 1
        else:
            # altrimenti incremento il valore corrente di 1
            vendite_categorie[categoria] += 1

# creo un insieme con le categorie disponibili (quelle che non sono vendute da nessun competitor)
categorie_disponibili = categorie - categorie_vendute

# print l`insieme delle categorie disponibili
print(f"Le categorie disponibili sono: {categorie_disponibili}")

# creo una lista di tuple (categoria, numero competitor che la vendono) dal dizionario delle vendite
vendite_categorie = [(categoria, vendite_categorie[categoria]) for categoria in vendite_categorie]

# print la lista delle vendite delle categorie,ordinandola in base alla categoria
print("Categorie vendute da competitor:")
for categoria, num_vendite in sorted(vendite_categorie, key=lambda x: x[0]):
    print(f"({categoria}, {num_vendite})")
