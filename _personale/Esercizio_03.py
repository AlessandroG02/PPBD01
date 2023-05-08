
    
#  metodo split() per dividere il testo in parole poi crea una nuova lista testo_censurato che sostituisce ogni parola incriminata con la censura usando una list dopo conta le parole censurate con un loop for che scorre la lista delle parole originali.
testo = """Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
base del tiramisù, prima classificata al premio Crema dell'Anno insieme
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
"""

parole = testo.split()
parola_malefica1 = "Tiramisù"
parola_malefica2 = "nutella"
censura = "******"
censurate = 0

testo_censurato = [censura if parola.lower() in (parola_malefica1.lower(),
                parola_malefica2.lower())
                else parola for parola in parole]

testo_censurato = ' '.join(testo_censurato)

for parola in parole:
    if parola.lower() in (parola_malefica1.lower(), parola_malefica2.lower()):
        censurate += 1

print(testo_censurato)
print(f"Censurate {censurate} parole")
