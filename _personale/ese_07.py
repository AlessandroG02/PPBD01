# freq associa a ciascuna lettera il numero di occorrenze di quella lettera
# trovate in tutta la lista

parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']

stringa = ''.join(parole)

lettere = set(stringa)
freq = {}

for k in lettere:
    contatore = stringa.count(k)
    freq[k] = contatore

print(freq)

# SECONDO MODO: senza usare set()
parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']

stringa = ''.join(parole)
freq = {}
conta = 0

for lettera in stringa: 
    conta = stringa.count(lettera)
    if lettera not in freq:
        freq[lettera] = conta
print(freq)





        
