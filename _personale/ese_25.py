'''# Si dispone di una stringa predefinita vocali che contiene tutte le lettere 
che designano i suoni delle vocali. Scrivete un programma che conti il numero 
di vocali nella variabile text e stampi questo numero.'''

vocali = 'aeiou'
text = "la volpe giallastra morde l'oca arancione, guuuuuuulp!" 
contatore = 0

for lettera in text:
    if lettera in vocali:
        contatore += 1

print('Ilnumero di vocali è:', contatore)