"""Esercizio - Festone di laurea
Requisiti: insiemi

Evviva! Ci siamo laureati! E per coincidenza ci siamo riusciti nella stessa sessione dei nostri grandi amici Gianni e Giulia. Ora naturalmente stiamo cercando di organizzare una festa e ci piacerebbe farla tutti insieme.

Purtroppo però a causa delle norme Covid non possiamo fare assembramento e sono perciò vietate i raduni con più di 13 persone.

Siccome ora siamo dottori, l'idea è quella di risolvere il problema con un bel programmino Python. Abbiamo tre liste di invitati e siccome noi festeggiati siamo tutti amici ci sono ovviamente persone che verrebbero invitate più volte.

Trova il numero di invitati effettivi (le persone che verranno alla festa)
Stampa la lista di nomi SENZA duplicati
Trova il numero delle persone che hanno ricevuto almeno 2 inviti
Trova l'elenco delle persone che hanno ricevuto almeno 2 inviti
Esempio - dati:

invitati_miei =   ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]
dopo il tuo codice, deve stampare:

Invitati miei:  6
Invitati gianni:  6
Invitati giulia:  7
Numero invitati:  11
Nomi invitati:  {'MassimilianoL', 'MartaB', 'MichelaF', 'EmmaK', 'GiorgioC', 'DavidL', 'VittorioG', 'SamanthaV', 'RobertoU', 'LucaB', 'GiuliaA'}
Numero amici invitati almeno 2 volte: 6
Amici invitati almeno due volte:  {'GiorgioC', 'DavidL', 'MichelaF', 'VittorioG', 'LucaB', 'EmmaK'}

# Input (NON modificare)

invitati_miei =   ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]

# scrivi qui
    """

# lista dei tre insiemi di invitati
invitati_miei = ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]

# unione dei tre insiemi in un unico insieme eliminando la duplicazione grazie al set()
invitati = set(invitati_miei + invitati_gianni + invitati_giulia)

# calcolo il numero di invitati effettivi (il numero di elementi dell`insieme invitati)
num_invitati = len(invitati)

# print il numero di invitati per ogni insieme di invitati e il numero totale di invitati effettivi
print("Invitati miei: ", len(invitati_miei))
print("Invitati gianni: ", len(invitati_gianni))
print("Invitati giulia: ", len(invitati_giulia))
print("Numero invitati: ", num_invitati)

# print l'insieme degli invitati senza duplicati utilizzando la funzione sorted() per ottenere una lista ordinata
print("Nomi invitati: ", set(sorted(invitati)))

# creo un insieme vuoto per memorizzare gli invitati che hanno ricevuto almeno 2 inviti
invitati_multipli = set()

# iter su tutti gli invitati dell`insieme invitati
for invitato in invitati:
    # conto il numero di volte che l`invitato appare negli insiemi di invitati originali
    count = 0
    if invitato in invitati_miei:
        count += 1
    if invitato in invitati_gianni:
        count += 1
    if invitato in invitati_giulia:
        count += 1
    # se l`invitato e` apparso almeno due volte lo aggiungiamo all`insieme degli invitati multipli
    if count >= 2:
        invitati_multipli.add(invitato)

# print numero amici invitati almeno due volte e l`insieme dei amici invitati almeno 2 volte
print("Numero amici invitati almeno 2 volte:", len(invitati_multipli))
print("Amici invitati almeno due volte:", invitati_multipli)

