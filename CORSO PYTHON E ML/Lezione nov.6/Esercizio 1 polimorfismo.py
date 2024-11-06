class MetodoPagamento:
    def __init__(self):
        self.__importo = None

    def effettua_pagamento(self, importo):
        self.__importo= importo

    def get_importo(self):
        return self.__importo

class CartaDiCredito(MetodoPagamento):
    def __init__(self):
        super().__init__()

    def effettua_pagamento(self,importo):
        super().effettua_pagamento(importo)
        print(f"Pagamento di {self.get_importo()} effettuato con carta di credito.")

class PayPal(MetodoPagamento):
    def __init__(self):
        super().__init__()

    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo) 
        print(f"Pagamento di {self.get_importo()} effettuato con Paypal")

class BonificoBancario(MetodoPagamento):
    def __init__(self):
        super().__init__()

    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo) 
        print(f"Pagamento di {self.get_importo()} effettuato con bonifico bancario.")


class GestorePagamenti:
    def __init__(self):
        pass

    def pagamento(self,modalità:MetodoPagamento,importo):
        modalità.effettua_pagamento(importo)

carta= CartaDiCredito()
bonifico=BonificoBancario()
paypal=PayPal()

pagare=GestorePagamenti()
pagare = GestorePagamenti()
pagare.pagamento(carta, 25)

pagare.pagamento(paypal, 50)
pagare.pagamento(bonifico, 100)
