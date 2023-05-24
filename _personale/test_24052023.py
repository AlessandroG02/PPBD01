import csv

match_attivita = 0

with open('./PPBD01/_personale/Comune-di-Torino---Attivita-commerciali.csv', 'r', encoding='utf-8') as file_in:
    mio_csv = csv.DictReader(file_in, delimiter=";")
    cap = [10126, 10127, 10134]
    for line in mio_csv:
        if int(line['Anno inizio attivita']) >= 2011 and line['Mq tot locale'].isdigit():
            if int(line['Mq tot locale']) >= 150 and int(line["Cap"]) in cap:
                match_attivita += 1

print(match_attivita)






