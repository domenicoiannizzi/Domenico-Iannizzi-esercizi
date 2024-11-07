class Dato:
    def __init__(self):
        self.numeri=[]
        self.stringhe=[]
        self.boolean=[]

    def aggiungi(self,lista):
        for dato in lista:
            if type(dato)== int:
                self.numeri.append(dato)
            elif type(dato) is bool:
                self.boolean.append(dato)

            else:
                self.stringhe.append(dato)

    def stampa_lista(self):
        print("Stampa la lista dei numeri : \n", self.numeri)
        print("Stampa la lista dei booleani: \n", self.boolean)
        print("Stampa la lista delle stringhe : \n", self.stringhe)




dati=Dato()
lista=[1,"ciao",True,"casa",False,34,"palla"]

dati.aggiungi(lista)
dati.stampa_lista()
                