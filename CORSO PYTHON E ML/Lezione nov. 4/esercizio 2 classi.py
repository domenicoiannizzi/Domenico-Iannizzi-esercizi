class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"libro '{self.titolo}' - autore: '{self.autore}' -: {self.pagine} pagine."
    
libro=Libro("a","b",43)
print(libro.descrizione())