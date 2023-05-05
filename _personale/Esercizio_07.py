"""Esercizio - dondolo
Requisiti: stringhe, dizionari, if, cicli

Scrivi del codice che data una lista di parole costituite solo dalla stessa lettera, crea un dizionario freq che associa a ciascuna lettera il numero di occorrenze di quella lettera trovate in tutta la lista

Esempio - data:

parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']
deve risultare:

>>> print(freq)
{'d': 8, 'o': 7, 'n': 3, 'l': 7}
parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']  # {'d': 8, 'o': 7, 'n': 3, 'l': 7}
# parole = ['d','ii','nnn','dd','ooo','n']                       # {'d': 3, 'i': 2, 'n': 4, 'o': 3}
             
# scrivi qui
    """

parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']

freq = {}

for parola in parole:
    for lettera in parola:
        if lettera not in freq:
            freq[lettera] = 1
        else:
            freq[lettera] += 1

print(freq)
