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

parola1 = parola_malefica1.casefold
parola2 = parola_malefica2.casefold
testo = testo.split(' ')
for parola in testo:
    if parola1 or parola2 in testo:
        testo_censurato = testo.replace(parola, censura)

print(testo_censurato)

