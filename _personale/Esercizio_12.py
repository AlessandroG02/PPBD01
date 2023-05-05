"""Esercizio - Elettromania
Produrre una sequenza con tutti i nomi dei componenti con più di 4 pezzi

NON USARE cicli for o while
USA UNA sola list comprehension
il tuo codice deve stare in una riga sola
INPUT: [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), ('trasduttore',2), ('transistor',12) , ('sensore',3),('solenoide',10)]

OUTPUT: ['condensatore', 'led', 'transistor' 'solenoide']


circuito = [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), ('trasduttore',2),
            ('transistor',12) , ('sensore',3),('solenoide',10)]

# scrivi qui

    """
    
circuito = [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), ('trasduttore',2),
            ('transistor',12) , ('sensore',3),('solenoide',10)]

componenti_piu_di_4 = [componente[0] for componente in circuito if componente[1] > 4]

print(componenti_piu_di_4)