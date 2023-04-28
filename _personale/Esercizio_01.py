"""
    Esercizio - Convertitori di grandezze
Convertire la temperatura da Fahrenheit a Celsius nella funzione sottostante. È possibile utilizzare questa formula:

 
Arrotondare il risultato restituito a 3 cifre decimali.

Non è necessario gestire l'input, basta implementare la funzione sottostante.

Inoltre, assicurarsi che la funzione restituisca il valore. NON stampare nulla.


def fahrenheit_to_celsius(f):
    ...
     
Passiamo al livello successivo della conversione di miglia in chilometri! Definite una funzione che accetti il numero di miglia e restituisca la distanza in chilometri.

Supponiamo che un miglio sia approssimativamente uguale a 1,609 chilometri.

Non è necessario gestire l'input, basta implementare la funzione.


def mi_to_km():
    ... 

"""

def fahrenheit_to_celsius(fahrein):
    celsius = (fahrein - 32) * 5/9
    return round(celsius, 3)

def mi_to_km(miles):
    km = miles * 1.609
    return km
