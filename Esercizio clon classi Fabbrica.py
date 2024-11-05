class Prodotto:
    def __init__(self,nome,costo_produzione,prezzo_vendita):   
        self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita
       
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Fabbrica:
    def __init__(self,inventario):
        self.inventario = {}
    
    def aggiungi_prodotto(self,prodotto,numero):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] +=numero
        else:
          self.inventario[prodotto.nome] =numero

    def vendi_prodotto(self,prodotto,numero):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] > 0:
            self.inventario[prodotto.nome] -= numero 
            profitto = prodotto.calcola_profitto() * numero
            print(f"Vendite effettuate:  {numero} per il prodotto: {prodotto.nome} con profitto di euro {profitto}")
        else:
            print("Vendita non completata ")

    def resi_prodotto(self,prodotto,numero):
        pass

prodotto=Prodotto("Lampade",325,466)

fabbrica=Fabbrica()

fabbrica.aggiungi_prodotto(prodotto,28)
print("Prodotti dopo aggiunta in inventario:  \n" ,fabbrica.inventario)

fabbrica.vendi_prodotto(prodotto,4)
print("Inventario post vendite : \n",fabbrica.inventario) 

fabbrica.resi_prodotto(prodotto,2)
print("Prodotti in inventario dopo il reso : ", fabbrica.inventario) #non resistuisce nulla di nuovo dopo il pass

        



