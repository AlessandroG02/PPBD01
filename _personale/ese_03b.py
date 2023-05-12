testo = """Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù, prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

parola_malefica1 = "Tiramisù"
parola_malefica2 = "nutella"

def change_case(convertibile):
    convertito = convertibile.lower()
    return convertito

testo2 = change_case(testo)
nuova_parola1 = change_case(parola_malefica1)
nuova_parola2 = change_case(parola_malefica2)

censura1 = len(nuova_parola1) * '*'
censura2 = len(nuova_parola2) * '*'

testo3 = testo2.replace(nuova_parola1, censura1)
testo3 = testo3.replace(nuova_parola2, censura2)


conteggio = testo2.count(nuova_parola1) + testo2.count(nuova_parola2)

print(testo3, '\n', 'Censurate', conteggio, 'parole.')

# vorrei poter fare il conteggio alla fine usando censura1 e censura2, però
# mi dà conteggio= 10 perchè quando faccio count(censura2) conta anche le censura1