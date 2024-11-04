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

    def cerca(self,per_cosa,risposta):
        cerca=[libro for libro in self.lista_libri if libro[per_cosa]== libro [risposta]]
        print(f"Libro trovato in base a {per_cosa} e {risposta}")
        for libro in cerca:
                print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, Pagine: {libro['pagine']}")
           
        

biblioteca = Biblioteca()
numero=int(input("Quanti libri vuoi inserire ?"))
for i in range(0,numero):
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    pagine = input("Inserisci il numero di pagine del libro: ")
    
    biblioteca.inserisci(titolo,autore,pagine)

biblioteca.stampa()
per_cosa=input("Cerchi libro per titolo o per autore?")
risposta=input("Inserisci titolo/autore da cercare")
biblioteca.cerca(per_cosa,risposta)
