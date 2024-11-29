'''Descrizione:  Crea un programma in Python per gestire una semplice libreria di libri. Il programma dovrebbe presentare un menu all'utente con le seguenti opzioni:
Aggiungere un nuovo libro: L'utente può inserire il titolo, l'autore e l'anno di pubblicazione del libro e quantità.
Visualizzare tutti i libri: Mostra una lista di tutti i libri attualmente nella libreria.
Cercare un libro per titolo: L'utente inserisce un titolo e il programma cerca e mostra i dettagli del libro se trovato.
Gestione libri: Far rimuovere modificare e/o aggiungere una compia in più del libro
Uscire dal programma: Termina l'esecuzione del programma'''



class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita
libri = []

def aggiungi_libro():
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    anno = int(input("Inserisci l'anno : "))
    quantita = int(input("Inserisci la quantità: "))
    nuovo_libro = Libro(titolo, autore, anno, quantita)
    libri.append(nuovo_libro)
    print("Libro aggiunto con successo!")

def visualizza_libri():
    if not libri:
        print("La libreria è vuota.")
    else:
        for libro in libri:
            print(libro)
def cerca_libro():
    titolo = input("Inserisci il titolo da cercare: ")
    for libro in libri:
        if libro.titolo == titolo:
            print(libro)
            return
    print("Libro non trovato.")
def gestisci_libro():
    titolo = input("Inserisci il titolo del libro da gestire: ")
    for libro in libri:
        if libro.titolo == titolo:
            print("1. Rimuovi libro")
            print("2. Modifica libro")
            print("3. Aggiungi copia")
            scelta = input("Scegli un'opzione: ")
            if scelta == '1':
                libri.remove(libro)
                print("Libro rimosso.")
            elif scelta == '2':
                print("Modifica non ancora implementata.")
            elif scelta == '3':
                libro.quantita += 1
                print("Copia aggiunta.")
            else:
                print("Libro non trovato.")

while True:
    print("\n Libreria ")
    print("1. Aggiungi un nuovo libro")
    print("2. Visualizza tutti i libri")
    print("3. Cerca un libro per titolo")
    print("4. Gestisci un libro")
    print("5. Esci")
    scelta = input("Scegli un'opzione: ")

    if scelta == '1':
        aggiungi_libro()
    elif scelta == '2':
        visualizza_libri()
    elif scelta == '3':
        cerca_libro()
    elif scelta == '4':
        gestisci_libro()
    elif scelta == '5':
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida.")