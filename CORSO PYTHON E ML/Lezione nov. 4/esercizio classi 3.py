class Biblioteca:
    def __init__(self):
        self.lista_libri=[]

    def inserisci(self,titolo,autore,pagine):
       libro = {
            "titolo": titolo,
            "autore": autore,
            "pagine": pagine
        }
       self.lista_libri.append(libro)

    def stampa(self):
        if len(self.lista_libri) !=0 :
            print("La biblioteca contiene : \n", self.lista_libri)
        else:
            print("Biblioteca vuota")

    def cerca_in(self):
        modalità = input(" Per cosa vuoi ricercare il libro ? ")
        if modalità.lower() in ["titolo","autore"]:
            cerca=input(f"Inserisci {modalità} che vuoi cercare :  ")
            risultati = [libro for libro in self.lista_libri if libro[modalità] == cerca]
            if len(risultati) >0:
                for libro in risultati:
                    print(libro)
            else:
                print("Non ha trovato nulla per questa ricerca")
        else:
            print("Devi cercare per titolo o autore")

    

biblioteca = Biblioteca()
numero=int(input("Quanti libri vuoi inserire ?"))
for i in range(0,numero):
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    pagine = input("Inserisci il numero di pagine del libro: ")
    
    biblioteca.inserisci(titolo,autore,pagine)

biblioteca.stampa()
biblioteca.cerca_in()
