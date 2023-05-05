"""Esercizio - Strambilia
Requisiti: list comprehension, zip

Si narra che la valle incantata di Strambilia sia popolata da innumerevoli specie fantastiche. La leggenda dice che chi riuscirà a nominarle tutte riceverà il fantomatico Dono Del Coding.

Nelle tue ricerche trovi un'antichissima pergamena che recita una lista delle specie, ma ahimè scopri che è incorretta. Per ottenere la lista giusta, vi sono allegate delle strane istruzioni:

Per ogni nome ottenere le prime 4 lettere e combinarle con le lettere dopo la quarta trovate nel nome corrispondente della lista rovesciata

NON USARE cicli for o while
NON USARE metodi delle liste (quindi niente .reverse() !)
Scrivi del codice che produce una NUOVA lista.

Esempio - data:

fauna = ["cippimerli",
         "gufolanti",
         "branchisauri",
         "cumulognembi",
         "arzigovolanti",
         "rotototteri",
         "barbagianni"]
il tuo codice deve produrre:

['cippagianni',
 'gufototteri',
 'brangovolanti',
 'cumulognembi',
 'arzichisauri',
 'rotolanti',
 'barbimerli']

fauna = ["cippimerli","gufolanti","branchisauri","cumulognembi","arzigovolanti","rotototteri","barbagianni"]
#produce: ['cippagianni','gufototteri','brangovolanti','cumulognembi','arzichisauri','rotolanti','barbimerli']

#fauna = ["ciospoloni", "sgarapirri", "rimbalammi", "tontoolonti", "zerbalonti", "gnampirilli"]
#produce:  ['ciospirilli', 'sgaralonti','rimboolonti','tontalammi','zerbapirri','gnampoloni']

# scrivi qui

    """
    
    
    

fauna = ["cippimerli","gufolanti","branchisauri","cumulognembi","arzigovolanti","rotototteri","barbagianni"]

nuova_fauna = [nome[:4] + nome_rev[4:] for nome, nome_rev in zip(fauna, reversed(fauna))]

print(nuova_fauna)
