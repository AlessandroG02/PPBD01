LUNGHEZZA_ETICHETTA = 48

num_canzone = 4   
# Into the Void _________________________________
# num_canzone = 10   
# Journey of 1,000 Years ________________________

kiss_album = """Psycho Circus _________________________________
Within ________________________________________
I Pledge Allegiance to the State of Rock & Roll
Into the Void _________________________________
We Are One ____________________________________
You Wanted the Best ___________________________
Raise Your Glasses ____________________________
I Finally Found My Way_________________________
Dreamin _______________________________________
Journey of 1,000 Years ________________________"""

# calcolazione l'inizio e la fine della riga che corrisponde  alla canzone
inizio_riga = (num_canzone - 1) * (LUNGHEZZA_ETICHETTA + 1)
fine_riga = inizio_riga + LUNGHEZZA_ETICHETTA

# prendo la sottostringa corispondente alla riga della canzone
riga_canzone = kiss_album[inizio_riga:fine_riga]

# print numero della canzone e la riga corispondente
print("numero canzone:", num_canzone)
print(riga_canzone)
