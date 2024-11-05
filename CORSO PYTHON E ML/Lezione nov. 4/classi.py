class Automobile:
    numero_ruote= 4
    def __init__(self,marca,modello):
        self.marca= marca
        self.modello=modello
    def stampa_info(self):
        print("L'automobile è " , self.marca, self.modello)

auto_1= Automobile("Fiat" , "500")
auto_1.stampa_info()