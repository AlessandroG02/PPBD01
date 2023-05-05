"""Esercizio - cannocchiale
Requisiti: tuple, stringhe, liste

Data una stringa s, scrivi del codice che mette in una variabile tupla ordinata tutti i caratteri di s ordinati

Esempio - data:

s = "cannocchiale"
Dopo il tuo codice deve risultare:

>>> print(ordinata)
('a', 'a', 'c', 'c', 'c', 'e', 'h', 'i', 'l', 'n', 'n', 'o')

s = "cannocchiale"

# scrivi qui

    """
    
s = "cannocchiale"
lista_caratteri = list(s)   # converto la stringa in una lista di caratteri
lista_caratteri.sort()      # ordino la lista
ordinata = tuple(lista_caratteri)  # converto la lista in una tupla
print(ordinata)
