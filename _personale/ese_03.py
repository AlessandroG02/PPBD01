testo = """Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù, prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

parola_malefica1 = "Tiramisù"
parola_malefica2 = "nutella"
parola_1_var1 = parola_malefica1.upper()
parola_1_var2 = parola_malefica1.lower()
parola_2_var1 = parola_malefica2.upper()
parola_2_var2 = parola_malefica2.lower()
 
parola_malefica01 = [parola_malefica1, parola_1_var1, parola_1_var2]
parola_malefica02 = [parola_malefica2, parola_2_var1, parola_2_var2]
censura = "******"
testo_censurato = ''

testo2 = testo.split(" ")
for parola in testo2:
    if parola in parola_malefica01 or parola_malefica02:
        testo_censurato = testo2.replace(parola, censura)


print(testo_censurato)


# secondo tentativo:
parole_proibite = []

def all_cases(maiu, minu):
    a = maiu.upper()
    b = minu.lower()
    return a, b

all_cases(parola_malefica1)
parola_malefica1.append(a)



#terzo tentativo:

parola1 = parola_malefica1.casefold
parola2 = parola_malefica2.casefold
testo = testo.split(' ')
for parola in testo:
    if parola1 or parola2 in testo:
        testo_censurato = testo.replace(parola, censura)

print(testo_censurato)


# usando lambda
