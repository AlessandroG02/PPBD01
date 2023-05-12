testo = """Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù, prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

parola_malefica1 = "Tiramisù"
parola_malefica2 = "nutella"
censura = "******"

def change_case(convertibile):
    convertito = convertibile.lower()
    return convertito

testo2 = change_case(testo)
nuova_parola1 = change_case(parola_malefica1)
nuova_parola2 = change_case(parola_malefica2)


testo3 = testo2.replace(nuova_parola1, censura)
testo3 = testo3.replace(nuova_parola2, censura)

conteggio = testo3.count(censura)


print(testo3, '\n', 'Censurate', conteggio, 'parole.')