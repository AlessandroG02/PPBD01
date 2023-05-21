indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]

lista = [f'ci sono {capi[indumenti.index(elemento)]} {elemento}' for elemento in indumenti]

print(lista)