'''Trova il numero di invitati effettivi (le persone che verranno alla festa)
Stampa la lista di nomi SENZA duplicati
Trova il numero delle persone che hanno ricevuto almeno 2 inviti
Trova l'elenco delle persone che hanno ricevuto almeno 2 inviti'''

invitati_miei =   ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA", "VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG", "RobertoU", "EmmaK"]

liste = invitati_miei + invitati_gianni + invitati_giulia
invitati = set(liste)
num_invitati =  len(invitati)

inviti_doppi = {}
for nome in invitati:
    contatore = liste.count(nome)
    if contatore >= 2:
        inviti_doppi[nome] = contatore

troppi_inviti = list(inviti_doppi.keys())

print('Numero invitati:', num_invitati, '\nNomi invitati:', invitati, '\nAmici invitati almeno due volte', troppi_inviti, '\nNumero amici invitati almeno 2 volte:', len(inviti_doppi))

