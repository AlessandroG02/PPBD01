"""Esercizio - Monte ordinato
Requisiti: liste, sort, for

Data una lista monte con 
 numeri (supponi che 
 sia pari), scrivi del codice che MODIFICA monte, ordinando solo i numeri nella prima metà in ordine crescente e poi ordinando solo i numeri nella seconda metà in ordine inverso

NON riassegnare monte, perchè perderesti la zona di memoria originale (quindi niente monte =)
SUGGERIMENTO: sort() funziona solo su tutta la lista, per ordinarne solo metà dovrai creare altre liste dove mettere i valori da ordinare, e poi copiarli nella lista originale
Esempio - data:

monte = [90,40,50,20,60, 7, 3, 4, 9, 8]
Dopo il tuo codice deve risultare:

>>> print(monte)
[20, 40, 50, 60, 90, 9, 8, 7, 4, 3]
monte = [90,40,50,20,60, 7, 3, 4, 9, 8]   # [20, 40, 50, 60, 90, 9, 8, 7, 4, 3]
#monte = [5,0,3,4,3,8]                    # [0, 3, 5, 8, 4, 3]
#monte = []                               # []
#monte = [7,3]                            # [7,3]

# scrivi qui
    """
monte = [90,40,50,20,60, 7, 3, 4, 9, 8]

# ordino la prima meta` in ordine crescente
meta1 = monte[:len(monte)//2]
meta1.sort()

# ordino la seconda meta` in ordine inverso
meta2 = monte[len(monte)//2:]
meta2.sort(reverse=True)

# copio i valori ordinati nella lista originale
monte[:len(monte)//2] = meta1
monte[len(monte)//2:] = meta2

print(monte)
