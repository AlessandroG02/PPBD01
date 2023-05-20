strumenti = [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), 
('trasduttore',2), ('transistor',12) , ('sensore',3),('solenoide',10)]

risultato = [elemento[0] for elemento in strumenti if elemento[1]> 4]

print(risultato)
      

