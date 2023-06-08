from inv.DataSender import DataSender
from inv.DataReciver import DataReciver

def main():
    # Menu che fa decidere all'utente quale processo eseguire
    while True:
        try:
            choice = input("Inserisci un'opzione ('Inviare' per inviare l'email con i candidati, "
                           "\n'Ricevere' per ricevere l'email ed aggiornare le richieste, "
                           "\n'Esci' per chiudere il programma: ")

            # Invia l'email dopo aver scelto la data e creato il file con i relativi CV
            if choice.lower() == "inviare":
                datasender = DataSender()
                print("Istanza di DataSender creata con successo.")
                datasender.send_data()
                print("Funzione send_data() della classe DataSender eseguita con successo.")

            # Dopo aver ricevuto l'email dalla sede centrale aggiunge le nuove richieste
            elif choice.lower() == "ricevere":
                datareceiver = DataReciver()
                print("Istanza di DataReceiver creata con successo.")
                datareceiver.reciver_data()
                print("Funzione receive_data() della classe DataReceiver eseguita con successo.")

            # Chiude il programma una volta che ha deciso di finire
            elif choice.lower() == "esci":
                print("Uscita dal programma...")
                break

            else:
                print("Opzione non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore durante l'esecuzione:")
            print(str(e))

if __name__ == "__main__":
    main()
