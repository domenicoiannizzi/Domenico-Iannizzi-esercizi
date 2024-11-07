class Aggregazione:
    def __init__(self):
        self.numeri = [2] * 5


    def valorizza_lista(self):
        i=0
        while i < 5:
                z=int(input("Inserisci numero "))
                self.numeri[i]= z
                if len(self.numeri) == 5:
                     break
                
                

    def somma(self, lista2):
         somma = []
         for i in range(5):  
            somma.append(self.numeri[i] + lista2.numeri[i])  
            return somma

while True: 
    lista1=Aggregazione()
    lista2=Aggregazione()
    lista1.valorizza_lista()
    lista2.valorizza_lista()
    somma = lista1.somma(lista2)

    
         
