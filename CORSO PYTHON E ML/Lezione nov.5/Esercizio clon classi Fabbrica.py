class Prodotto:
    def __init__(self,nome,costo_produzione,prezzo_vendita):   
        self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita
       
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
    def get_prezzo_vendita(self):   # getter e setter per prezzo di vendita
        return self.__prezzo_vendita
             
    def set_prezzo_vendita(self, prezzo_vendita):   
        self.__prezzo_vendita = prezzo_vendita
        print("Prezzo vendita : ", prezzo_vendita)
    
    def info_prodotto(self):       #aggiunta di info_prodotto per essere poi richiamato
        return f"Prodotto: {self.nome} in vendita al prezzo di : {self.prezzo_vendita}"
    
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        super().__init__(nome, costo_produzione, prezzo_vendita)
    
    
class Sport(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        super().__init__(nome, costo_produzione, prezzo_vendita)

    
class Fabbrica:
    def __init__(self, inventario=None):
        inventario= {}
        self.inventario = inventario
    
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
elettronica=Elettronica("Tv",211,1010)
sport=Sport("Racchetta",11,21)

elettronica.set_prezzo_vendita(850)  #metodo set richiamato

fabbrica=Fabbrica()

fabbrica.aggiungi_prodotto(elettronica,28)                                  
print("Prodotti dopo aggiunta in inventario:  \n" ,fabbrica.inventario) 
fabbrica.vendi_prodotto(elettronica,2)

print("Inventario post vendite : \n",fabbrica.inventario) 

fabbrica.resi_prodotto(prodotto,2)
print("Prodotti in inventario dopo il reso : ", fabbrica.inventario) #non resistuisce nulla di nuovo dopo il pass

        
print(sport.info_prodotto())  #info_prodotto richiamato

