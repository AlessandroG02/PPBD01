'''Data una lista monte con 
 numeri (supponi che 
 sia pari), scrivi del codice che MODIFICA monte, ordinando solo i numeri nella
 prima metà in ordine crescente e poi ordinando solo i numeri nella seconda metà
 in ordine inverso.
 NON riassegnare monte, perchè perderesti la zona di memoria originale (quindi
 niente monte =)
SUGGERIMENTO: sort() funziona solo su tutta la lista, per ordinarne solo metà 
dovrai creare altre liste dove mettere i valori da ordinare, e poi copiarli 
nella lista originale'''

monte = [90,40,50,20,60, 7, 3, 4, 9, 8]
half = int(len(monte)/2)

primo = monte[:half]
primo.sort()
secondo = monte[half:]
secondo.sort(reverse=True)

for numero in secondo:
    primo.append(numero)
    
print(primo)