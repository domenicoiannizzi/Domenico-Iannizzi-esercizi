class Ristorante:
    #inizializzo la classe ristorante
    def __init__(self,nome,tipo_cucina,aperto=False):
        self.nome=nome
        self.tipo_cucina=tipo_cucina
        self.aperto=aperto
        self.menu=None

    def aggiungi(self,diz):
        diz[self.nome]={
            "tipo_cucina": self.tipo_cucina,
            "aperto": self.aperto,
            "menu": self.menu.piatti if self.menu else []
        }

    #descrivo il ristorante con tipo di cucina

    def descrivi(self):
        
        return f"Il ristorante {self.nome} offre cucina {self.tipo_cucina} "
    
    #classe gestisci per modificare lo stato di apertura
class Gestisci:
        
    def __init__(self, ristorante):
        self.ristorante = ristorante
        stato = "aperto" if self.ristorante.aperto else "chiuso"
        print(f"Il ristorante '{self.ristorante.nome}' è attualmente {stato}")
    
    def apri(self):
        if not self.ristorante.aperto:
            self.ristorante.aperto = True
            print(f"Ristorante {self.ristorante.nome} aperto")
        else:
             print(f"Ristorante {self.ristorante.nome} chiuso")

    def chiudi(self):
        if self.ristorante.aperto:
            self.ristorante.aperto = False
            print(f"ristorante {self.ristorante.nome} chiuso")
        else:
            print(f"Il ristorante {self.ristorante.nome} è già chiuso")

#classe menu per gestire il menù aggiungengo e rimuovendo piatti, oltre a stamparlo
class Menu:
    def __init__(self,ristorante):
        self.piatti = []
        self.ristorante=ristorante
        ristorante.menu=self

    def add_piatti(self,nome_piatto):
         if nome_piatto not in self.piatti:
            self.piatti.append(nome_piatto)
            print(f"Piatto {nome_piatto} aggiunto al menu")
    
    def rem_piatti(self,nome_piatto):
        if nome_piatto in self.piatti:
            self.piatti.remove(nome_piatto)
            print(f"Piatto {nome_piatto} rimosso dal menu.")

    def stampa_menu(self):
            print("I piatti sono : \n " ,self.piatti)

 

dizionario_ristoranti = {} 

ristorante1 = Ristorante("Casa", "Italiana") 
print(ristorante1.descrivi())

gestisci= Gestisci(ristorante1) 
gestisci.apri()
menu=Menu(ristorante1)
menu.add_piatti("Pizza")
menu.add_piatti("Pasta al sugo")
menu.stampa_menu()
menu.rem_piatti("Pizza")
gestisci.chiudi()
ristorante1.aggiungi(dizionario_ristoranti)
print(dizionario_ristoranti)

        

