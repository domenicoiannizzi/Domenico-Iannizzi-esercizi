class Veicolo:
    def __init__(self,marca,modello):
        self.marca=marca
        self.modello=modello

    def mostra_info(self):
        print(f"Veicolo {self.modello}, marca {self.marca}")


class Dotazionispeciali:
    def __init__(self,dotazioni):
        self.dotazioni=dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")


#EREDITARIETA' SINGOLA
class Quad(Veicolo):
    pass


#EREDITARIETà MULTIPLA

class AutomobileSportiva(Veicolo, Dotazionispeciali):
    def __init__(self, marca, modello,dotazioni,cavalli):
        Veicolo.__init__(marca, modello)

        Dotazionispeciali.__init__(self,dotazioni)
        self.cavalli=cavalli

    def mostra_dotazioni(self):
        super().mostra_info()
         # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")


        self.mostra_dotazioni()


#utilizzo classi di derivazione 
auto_sportiva = AutomobileSportiva ("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)
auto_sportiva.mostra_informazioni()

