class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def suono(self):
         pass

class Gatti(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def suono(self):
        super().suono()
        print("Miaoooooo !!")

    def graffio(self):
        print(" Ti graffio amico, ops !")



class Conigli(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def suono(self):
        print("Boh, e chi lo sa il nome del suono")
    
    def carota(self):
        print("Dammi una carota, please")

class Delfino(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def suono(self):
        print("Fischia !")
    
    def salta(self):
        print("Guarda come emerge dall'acqua con un salto")



class Zoo:
    def __init__(self):
        self.diz_animali={} 


    def aggiungi(self,specie,animale):
        if specie not in self.diz_animali:
            self.diz_animali[specie]=[]
        self.diz_animali[specie].append(animale)

    def visualizza_zoo(self):
        for specie,lista in self.diz_animali.items():
            for animale in lista:
                print(f"Specie: {specie}, nome:{animale.nome}, età: {animale.eta}, suono: ")
                animale.suono()
                if specie.lower() == "gatto":
                    animale.graffio()
                if specie.lower() == "coniglio":
                    animale.carota()
                if specie.lower() == "delfino":
                    animale.salta()


gatto1=Gatti("Federico",26)
gatto2=Gatti("Mimmo",21)

zoo=Zoo()
zoo.aggiungi("gatto",gatto1)
zoo.aggiungi("gatto",gatto2)

zoo.visualizza_zoo()



        

