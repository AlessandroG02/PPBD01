# Esercizio di ricapitolazione

# Proviamo ora a scrivere un programma che prenda un singolo numero intero `n` ed esegua le seguenti operazioni nell'ordine indicato:

# 1. aggiunge `n` a se stesso;
# 2. moltiplica il risultato per `n`;
# 3. sottrae `n` dal risultato;
# 4. divide esattamente il risultato per `n` (cioè deve eseguire una divisione intera);
# 5. stampa il risultato della divisione. --> --> 

n = int(float(input('inserisci numero intero'))) 
# int(float mi permette di trasformare un eventuale input float in int troncando il dec) 
n = ((((n + n) * n) - n)/n)
new_n = int(n)
print(new_n)
 
