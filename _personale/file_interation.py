file = open('./files_esercizi/personaggi.txt', 'r', encoding='UTF-8')
print(file.read())
file.close()

file1 = open('./files_esercizi/outputs/test_write_1line.txt', 'w', encoding='utf-8')
file1.write('Questa è una riga in un file di prova!')
file.close()