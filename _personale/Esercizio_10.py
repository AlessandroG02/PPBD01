"""Esercizio - Guardaroba
Produrre una sequenza di stringhe combinando due di input.

NON usare range
USA UNA sola list comprehension
il tuo codice deve stare in una riga sola
Esempio - data:

indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]
Il tuo codice deve produrre:

['ci sono 9 cappotti', 'ci sono 5 giacconi', 'ci sono 7 mantelli', 
 'ci sono 3 ventine']

indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]

# scrivi qui

    """
indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]

result = ["ci sono " + str(capi[i]) + " " + indumenti[i] for i in range(len(indumenti))]

print(result)
