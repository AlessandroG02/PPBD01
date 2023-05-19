import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione f(x)
def f(x):
    return (x - 1) / (x**2 - 4)

# Definizione della funzione h(x)
def h(x):
    return np.exp(f(x))

# Creazione di un array di valori x da -5 a 5
x = np.linspace(-5, 5, 500)

# Calcolo dei valori corrispondenti di y
y = h(x)

# Creazione del grafico
plt.plot(x, y, label='h(x)')

# Aggiunta di etichette agli assi
plt.xlabel('x')
plt.ylabel('h(x)')

# Aggiunta di una legenda
plt.legend()

# Impostazione del colore rosso per la parte negativa di y
plt.fill_between(x, y, where=(y < 0), color='red', alpha=0.3)

# Impostazione del colore verde per la parte positiva di y
plt.fill_between(x, y, where=(y >= 0), color='green', alpha=0.3)

# Mostra il grafico
plt.show()
