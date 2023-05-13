#La lunghezza di ogni riga
lunghezza_etichetta = 48

# Il database contenente le canzoni# Il database contenente le canzoni
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

album = kiss_album.split('\n')
num_tracce = len(album)

richiesta = int(input("numero canzone: "))
if 1 < richiesta <= num_tracce:
    traccia = album[richiesta -1]
    print(traccia)
else:
    print('scegli una canzone compresa tra 1 e', num_tracce)