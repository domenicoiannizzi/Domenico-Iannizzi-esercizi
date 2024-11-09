class MetodoPagamento:
    def __init__(self,saldo=0):
        self.__importo = None
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,saldo):
        self.__saldo=saldo

    def effettua_pagamento(self, importo):
        if importo <= self.__saldo:
            self.__importo= importo
            self.__saldo -= importo

    def get_importo(self):
        return self.__importo

class CartaDiCredito(MetodoPagamento):
    def __init__(self,saldo):
        super().__init__(saldo)

    def __test_credenziali(self,numero,cvv,scadenza):
        return True

    def effettua_pagamento(self,importo):
        numero=int(input(("Inserisci numero carta :  ")))
        scadenza=int(input("Inserisci anno di scadenza : "))
        cvv=int(input("Inserisci cvv : "))

        if self.__test_credenziali(numero,cvv,scadenza):
            super().effettua_pagamento(importo)
            print(f"Pagamento di {self.get_importo()} effettuato con carta di credito.")
        else:
            print("Credenziali errate")


class PayPal(MetodoPagamento):
    def __init__(self,saldo):
        super().__init__(saldo)

    def __test_credenziali(email,psw):
        return True

    def effettua_pagamento(self, importo):
        email=input("Inserisci email :")
        psw=input("Inserisci password : ")
        if self.__test_credenziali(email,psw):
            super().effettua_pagamento(importo) 
            print(f"Pagamento di {self.get_importo()} effettuato con Paypal")

        else:
            print("Credenziali errate")

class BonificoBancario(MetodoPagamento):
    def __init__(self,saldo):
        super().__init__(saldo)
    
    def __test_credenziali(iban):
        return True

    def effettua_pagamento(self, importo):
        iban= int(input("Inserisci IBAN del conto bancario : "))

        if self.__test_credenziali(iban):
            super().effettua_pagamento(importo) 
            print(f"Pagamento di {self.get_importo()} effettuato con bonifico bancario.")

        else:
            print("IBAN errato")



class GestorePagamenti:
    def __init__(self):
        pass

    def pagamento(self,modalita: MetodoPagamento,importo):
       modalita.effettua_pagamento(importo)


saldo=int(input("inserisci saldo :"))
carta = CartaDiCredito(saldo)
paypal = PayPal(saldo)
bonifico = BonificoBancario(saldo)

gestore=GestorePagamenti()

while True:
    print("Scegli un metodo di pagamento:")
    print("1 - Carta di Credito")
    print("2 - PayPal")
    print("3 - Bonifico Bancario")
    print("q per uscire")
    scelta=input("Inserisci scelta da effettuare ")
    
    if scelta == "1":
        metodo=carta

    elif scelta == "2":
        metodo=paypal

    elif scelta == "3":
        metodo = bonifico

    elif scelta == "q":
        print("Esci")
        break

    else:
        print("Scelta non valida, riprova.")
        continue

    importo= float(input("inserisci importo : "))
    gestore.pagamento(metodo,importo)
    