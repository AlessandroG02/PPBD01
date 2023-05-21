'''Per ogni nome ottenere le prime 4 lettere e combinarle con le lettere dopo
 la quarta trovate nel nome corrispondente della lista rovesciata.
 NON USARE cicli for o while
 NON USARE metodi delle liste (quindi niente .reverse() !)'''
 
fauna = ["cippimerli",
         "gufolanti",
         "branchisauri",
         "cumulognembi",
         "arzigovolanti",
         "rotototteri",
         "barbagianni"]



prima_lista = [parola[:4]for parola in fauna]
seconda_lista = [parola[4:]for parola in fauna[-1::-1]]
terza_lista = [f'{any}{seconda_lista[prima_lista.index(any)]}' for any in prima_lista]

print(terza_lista)


