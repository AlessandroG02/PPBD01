"""
Esercizio - La ricetta della nonna
Requisiti: stringhe, liste, if, for, import,

La nonna ci ha dato la sua miracolosa ricetta della pasta olive acciughe e capperi.

Variante 1: Dobbiamo andare a comprare tutti gli ingredienti che appaiono nella lista più di una volta.

Variante 2: Dobbiamo andare a comprare gli ingredienti e dobbiamo capire quanti "cappero", "oliva" e "pepe" comprare. Di pasta e altri ingredienti ne abbiamo già in quantità, quindi non ci interessano.

ATTENZIONE: la nonna ha la sua età ed è sempre stata pasticciona e quindi la ricetta è scritta in modo non consistente, e le parole vanno normalizzate
SUGGERIMENTO: c'è un comodo metodo delle stringhe per separare le parole...
Esempio - dati:

ricetta = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
stampa:

  Servono:
     3 oliva
     2 pepe
     3 cappero

ricetta_orig = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
# ricetta = "oliva\t, pepe,cappero ,\n dete\nrsivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
# ricetta = "cappone , pepe,\noliva\n,\n\tpepe, acciuga "   #  1 oliva 2 pepe 0 cappero

# scrivi qui

"""

# VARIANTE 1
ricetta_orig = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"

# normalizzo la stringa della ricetta
ricetta = ricetta_orig.lower().replace('\n', '').replace('\t', '').replace(' ', '')

# divido la stringa in lista di ingredienti
ingredienti = ricetta.split(',')

# creazione dizionario per tenere traccia ingredienti gia` visti
ingredienti_visti = {}

# iter sulla lista degli ingredienti
for ingrediente in ingredienti:
    # se l'ingrediente non e` vuoto e non e` un ingrediente che e` stato  gia` visto lo aggiungo al dizionario
    if ingrediente not in ingredienti_visti and ingrediente != 'pasta' and ingrediente != 'pomodoro' and ingrediente != 'olio':
        ingredienti_visti[ingrediente] = 1
    # se l'ingrediente non e` vuoto e stato visto questo ingrediente in precedenza incrementa il suo contatore
    elif ingrediente in ingredienti_visti:
        ingredienti_visti[ingrediente] += 1

# stampa gli ingredienti che compaiono piu` di una volta
print("Dobbiamo comprare:")
for ingrediente, conteggio in ingredienti_visti.items():
    if conteggio > 1:
        print(f"{conteggio} {ingrediente}")



# VARIANTE 2
def ingredienti_da_comprare(ricetta):
    # normalizza la stringa della ricetta
    ricetta = ricetta.lower().replace('\n', '').replace('\t', '').replace(' ', '')

    # crea una lista di ingredienti
    ingredienti = ricetta.split(',')

    # crea un dizionario per tenere traccia delle quantita` di ciascun ingrediente
    quantità = {'oliva': 0, 'pepe': 0, 'cappero': 0}

    # scorre la lista di ingredienti e aggiorna il dizionario delle quantita`
    for ingrediente in ingredienti:
        if ingrediente in quantità:
            quantità[ingrediente] += 1

    # stampa le quantita` di ingredienti da comprare
    print("Servono:")
    for ingrediente, quantità in quantità.items():
        print(f"{quantità} {ingrediente}")
