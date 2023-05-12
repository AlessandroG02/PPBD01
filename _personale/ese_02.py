vecchia_ricetta = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga ,oliva , pepe\t,\t cappero , \noliva,pasta\n"
ricetta = vecchia_ricetta.replace('\n', '')
ricetta = ricetta.replace('\t', '')
ricetta = ricetta.replace(' ', '')


nuova_ricetta = ricetta.split(',')
ingredienti = set(nuova_ricetta)
quantita = 0

print('Servono:')
for ingr in ingredienti:
    quantita = nuova_ricetta.count(ingr)
    # print('Servono', quantita, ingr)  dà una lista di tutti gli ingredienti richiesti
    if quantita > 1:
        print(quantita, ingr)


    




