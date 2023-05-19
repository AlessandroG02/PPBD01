# Scrivi del codice che data una lista di parole costituite solo dalla stessa lettera, crea un
# dizionario freq che associa a ciascuna lettera il numero di occorrenze di quella lettera trovate 
# in tutta la lista

parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']
freq = {}
numero_lettere = []
for any in parole:
    singola_parola = str(any)
    lettere = len(singola_parola)
    # numero_lettere.append(lettere) non serve qui
    freq[singola_parola] = lettere

print(freq)

# """questo metodo è sbagliato perchè:
#   1. ignora il fatto che ci sono più parole formate dalla stessa lettera
#   2. la chiave è costituita dall'intera stringa di ripetizione e non da una lettera singola"""


# SECONDO tentativo
parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']

stringa = ''.join(parole)
freq = {}
conta = 0
# print(stringa)
for lettera in stringa:
    print(lettera)
    conta = stringa.count(lettera)
    if lettera not in freq:
        freq = dict[lettera] = conta
print(freq)


