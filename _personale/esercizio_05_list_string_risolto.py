# LUNGHEZZA_ETICHETTA = 48

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

# num_song = 4    #  Into the Void _________________________________
# num_song = 10   #  Journey of 1,000 Years ________________________
num_song = int(input('Inserire il numero della canzone:'))  

list_songs = kiss_album.split('\n')              
qta_canzoni = len(list_songs)                     

if 1 <= num_song and num_song <= qta_canzoni:  
# if 1 <= num_song <= qta_canzoni:                
# if (num_song - 1) in range(qta_canzoni):        
    nome_canzone = list_songs[num_song - 1]    
                                                     
    print('numero canzone:', num_song)            
    print(nome_canzone)                              
else:                                                
    print('Si prega di inserire un numero tra 1 e', qta_canzoni)  