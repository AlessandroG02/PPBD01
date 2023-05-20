''' Input: Leggere una parola o una frase scritta in minuscoloCamelCase
Output: Stampa le parole in minuscolo, separate da trattini bassi.

SUGGERIMENTO: I metodi delle stringhe str.lower(), str.isupper() (o str.islower())
 potrebbero tornarti utili. Se non li conosci, vai a leggere la documentazione.'''
 
word = input()
lista = list(word)
word_snaked = list()

for lettera in lista:
    if lettera.islower():
        word_snaked.append(lettera)
    else:
        # print(lettera)
        word_snaked.append('_')
        lettera_low = lettera.lower()
        word_snaked.append(lettera_low)
        # print(lettera_snaked)

if word_snaked[0] == '_':
    word_snaked.remove('_')
snake_case = ''.join(word_snaked)             
print(snake_case)