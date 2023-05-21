categorie = {"Ferramenta", "Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Cosmetici", "Pesce", "Alcolici", "Forniture Elettriche", "Telefonia"}
competitor = [
        ("GenerStore", {"Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Pesce", "Alcolici"}),
        ("MomentiElettrizzanti", {"Abbigliamento sportivo", "Videogames", "Gioielleria", "Alcolici", "Forniture Elettriche"}),
        ("TuttoEDiPiù", {"Videogames", "Gioielleria", "Pesce", "Alcolici", "Forniture Elettriche"}),
        ("ProfumoDiBuono", {"Pesce", "Alcolici", "Forniture Elettriche"}),
        ("PessimeCombo", {"Alcolici", "Telefonia"}),
]

'''"Le categorie disponibili sono: {b, f}"
Categorie vendute da competitor:'''

disponibile = []
lista_occupati = []
dizionario = {}

occupato =[list(elemento[1]) for elemento in competitor]

for any in occupato:
    for elemento in any:
        lista_occupati.append(elemento)

for cat in categorie:
    if cat not in lista_occupati:
        disponibile.append(cat)
        
for elemento in categorie:
    conta = lista_occupati.count(elemento)
    if conta > 0:
        dizionario[elemento] = conta

print('Le categorie disponibili sono:', disponibile)
print('Categorie vendute da competitor:', dizionario)

