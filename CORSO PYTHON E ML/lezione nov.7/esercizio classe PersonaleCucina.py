class PersonaleCucina:
    def __init__(self,nome,eta,ordini_possibili=0,serviti=0):
        self.__nome=nome
        self.__eta=eta
        self.ordini_possibili=ordini_possibili
        self.serviti= serviti

    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta
    
    def lavora():
        pass

    def stampa_info():
        pass

class Chef(PersonaleCucina):
    def __init__(self, nome, età,specialita,ordini_possibili,serviti=0):
        super().__init__(nome, età,ordini_possibili,serviti)
        self.__specialita=specialita
        self.piatti=["Pasta al sugo" , "Lasagne"]

    def get_specialita(self):
        return self.__specialita

    def lavora(self):
        print(f"Lo chef {self.get_nome()} cucina e prepara il menù")

    def prepara_menu(self):
          return f"Chef{self.get_nome()} cucina e prepara {self.__specialita}"

    def stampa_info(self):
        print(f"Nome {self.get_nome()}, Età {self.get_eta()}, Ruolo: Chef, Specialità: {self.__specialita}")

    def serve_piatto(self, piatto, ristorante):
        if piatto in self.piatti:
            for nome_piatto, ingredienti in ristorante.menu:
                if nome_piatto == piatto:
                    self.serviti += 1
                    return f"{self.get_nome()} sta preparando il piatto: {piatto}"
                return f"{self.get_nome()} non prepara il piatto: {piatto}"
                    
      
    

class SousChef(PersonaleCucina):
    def __init__(self, nome, eta,ordini_possibili,serviti=0):
        super().__init__(nome, eta,ordini_possibili,serviti)
        self.piatti=["Ragù", "Pizza"]

    def gestisci_inventario(self,ristorante):
        for ingredienti in ristorante.menu:
            print(ingredienti)

    def lavora(self):
        print(f" Il SousChef {self.get_nome()} assiste lo chef e gestisce inventario")

    def stampa_info(self):
        print(f"Nome {self.get_nome()}, Età {self.get_eta()}, Ruolo: SousChef")

    def serve_piatto(self, piatto, ristorante):
        if piatto in self.piatti:
            for nome_piatto, ingredienti in ristorante.menu:
                if nome_piatto == piatto:
                    self.serviti += 1
                return f"{self.get_nome()} sta preparando il piatto: {piatto}"
        return f"{self.get_nome()} non prepara il piatto: {piatto}"
    
    
class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta,nome_piatto,ordini_possibili,serviti=0):
        super().__init__(nome, eta,ordini_possibili,serviti)
        self.__nome_piatto=nome_piatto
        self.piatti=["Carbonara", "Cotoletta alla milanese"]


    def get_nomepiatto(self):
        return self.__nome_piatto

    def lavora(self):
        print(f"Il Cuoco di linea {self.get_nome()}  cucina.")

    def stampa_info():
        print(f"Nome: {self.get_nome()}, Età: {self.get_eta()}, Ruolo: Cuoco di Linea")


    def cucina_piatto(self):
        for self.__nome_piatto in self.piatti:
            print(f"{self.get_nome()} sta preparando il piatto {self.get_nomepiatto}")

    def serve_piatto(self, piatto, ristorante):
        if piatto in self.piatti:
            for nome_piatto, ingredienti in ristorante.menu:
                if nome_piatto == piatto:
                    self.serviti += 1
                    return f"{self.get_nome()} sta preparando il piatto: {piatto}"
        return f"{self.get_nome()} non prepara il piatto: {piatto}"
    
class Ristorante:
    def __init__(self):
        self.menu= []
        self.ordinazioni=[]

    def aggiungi_piatto(self, nome_piatto, ingredienti):
        self.menu.append((nome_piatto, ingredienti))
        print(f"Piatto '{nome_piatto}' aggiunto al menu con ingredienti: {', '.join(ingredienti)}")

    def prendi_ordinazione(self,cliente, nome_piatto):
        self.ordinazioni.append((nome_piatto))
        print(f"Ordinazione del {cliente.nome} aggiunta per il piatto : {nome_piatto}'.")

    
    def visualizza_menu(self):
        print("Menu del ristorante:")
        for piatto, ingredienti in self.menu:
            print(f" {piatto}: {ingredienti}")


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.ordinazioni = []

    def ordina(self, nome_piatto, ristorante):
        print(f"{self.nome} ordina :{nome_piatto}")
        ristorante.prendi_ordinazione(self, nome_piatto)
        self.ordinazioni.append(nome_piatto)

        for nome_piatto in self.ordinazioni:
            if nome_piatto not in ristorante.menu:
                self.ordinazioni.remove(nome_piatto)
                ristorante.ordinazioni.remove(nome_piatto)
                

        
    
           
ristorante = Ristorante()
ristorante.aggiungi_piatto("Pasta al sugo", ["spaghetti", "pomodoro", "basilico", "olio"])
ristorante.aggiungi_piatto("Lasagne",["pomodoro", "pasta", "olio"])

cliente1 = Cliente("Giovanni")
cliente1.ordina("Pasta al sugo", ristorante)
cliente1.ordina("Pizza Margherita", ristorante)

chef = Chef("domenico", 45, "Pasta al sugo", ordini_possibili=4)
sous_chef = SousChef("massimo", 25, ordini_possibili=3)
cuoco_linea = CuocoLinea("luca","carbonara", 30, ordini_possibili=10)
ristorante.visualizza_menu()



print(chef.serve_piatto("Pasta al sugo",ristorante))

    
    