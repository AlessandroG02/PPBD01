LUNGHEZZA_ETICHETTA = 48

num_canzone = 7   
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

# # calcolazione l'inizio e la fine della riga che corrisponde  alla canzone
# inizio_riga = (num_canzone - 1) * (LUNGHEZZA_ETICHETTA + 1)
# fine_riga = inizio_riga + LUNGHEZZA_ETICHETTA

# # prendo la sottostringa corispondente alla riga della canzone
# riga_canzone = kiss_album[inizio_riga:fine_riga]

# # print numero della canzone e la riga corispondente
# print("numero canzone:", num_canzone)
# print(riga_canzone)

continua = True

while continua:
    try:
        track_num_user = int(input("Inserire numero canzone desiderata (max canzone 10): "))
        if track_num_user < 1 or track_num_user > 10:
            raise ValueError
        track_num_py = track_num_user - 1
        list_album = kiss_album.split("\n")
        print("Numero canzone:", track_num_py + 1)
        print(list_album[track_num_py])
        continua = False
    except ValueError:
        print("Errore: Inserire un numero intero valido compreso tra 1 e 10.")
    except IndexError:
        print("Errore: Numero canzone non valido. Riprovare.")

    scelta = input("Desideri continuare? (sì/no): ")
    if scelta.lower() != "sì" and scelta.lower() != "si":
        continua = False
        print("Grazie per aver utilizzato il programma. Arrivederci!")
