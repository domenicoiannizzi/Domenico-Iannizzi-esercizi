class ContoBancario:
    def __init__(self, titolare, saldo=0):
        self.__titolare = titolare
        self.__saldo= saldo if saldo >0 else 0

    def titolare(self):                 #getter titolare
        return self.__titolare
    
    def set_titolare(self,titolare1):    #setter titolare
        if len(titolare1) !=0:
            self.__titolare= titolare1
            print("Il titolare è : ", titolare1)
        else:
           print("Il nome del titolare deve essere una stringa non vuota.")

    def visualizza_saldo(self):         
        return self.__saldo
    
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di € {importo}. Saldo attuale: {self.__saldo}")

    def preleva(self,importo):
        if importo >0 and importo<= self. __saldo:
            self.__saldo -= importo
            print(f"Prelievo di € {importo}. Saldo attuale: {self.__saldo}")

    
conto = ContoBancario("Domenico",2650)
print(conto.visualizza_saldo())
conto.deposita(1050)
conto.preleva(350)
print(conto.visualizza_saldo())
conto.set_titolare("Giacomo")


