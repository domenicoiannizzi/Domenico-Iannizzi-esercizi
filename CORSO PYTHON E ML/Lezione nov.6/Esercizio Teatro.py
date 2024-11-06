class Posto:
    def __init__(self, numero, fila):
        self.__numero = numero         
        self.__fila = fila              
        self.__occupato = False  
    
    def prenota(self):
        if not self.__occupato:
            self.__occupato = True
            print(f"Posto prenotato : numero {self.numero}, fila {self.fila}")
        else:
            print("Posto occupato")

    def libera(self):
        if self.__occupato:
            self.__occupato = False
            print(f"Posto libero: {self.numero} - {self.fila}")

    def get_numero(self):       #getter per il numero
        return self.__numero

    def get_fila(self):       #getter per il posto
        return self.__fila

    def occupazione(self):               #mi restituisce True o False se è occupato o meno
        return self.__occupato
        
class PostoVip(Posto):
    def __init__(self, numero, fila,serviziovip):
        super().__init__(numero, fila)
        self.__serviziovip= serviziovip

    def prenota(self):
        super().prenota()
        if self.occupazione():
            print(f"Servizio extra per il posto vip:{self.__serviziovip} ")

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_aggiuntivo=0):
        super().__init__(numero, fila)
        self.__costo_aggiuntivo = costo_aggiuntivo

    def aggiuntivo(self):                           #metodo get per il costo aggiuntivo
        return self.__costo_aggiuntivo

class Teatro:
    massimo=10
    def __init__(self):
        self.__posti = []

    def add_posto(self,posto):
        if len(self.__posti) < Teatro.massimo:
            self.__posti.append(posto)

    def prenota(self,numero,fila):
        for posto in self.__posti:
                if posto.get_numero() == numero and posto.get_fila() == fila :
                    if not posto.occupazione():
                        posto.prenota()
                else:
                    print("numero massimo raggiunto.")


    def stampa_posti(self):
        for posto in self.__posti:
            stato = "Occupato" if posto.occupazione() else "Libero"
            print(f"Fila: {posto.get_fila()}, Numero: {posto.get_numero()}, Stato: {stato}")



teatro=Teatro() #crea oggetto teatro
numero = int(input("Quanti posti vuoi inserire nel teatro ? "))
for i in range(numero):
        tipo_posto = input("Vuoi aggiungere un posto VIP o Standard?").strip().lower()
        fila = input("Inserisci la fila del posto: ").strip()
        numero1= int(input("Inserisci il numero del posto: "))

        if tipo_posto == "vip":
            serviziovip = input("Inserisci il servizio vip ")
            posto = PostoVip(numero, fila, serviziovip)

        else:
            costo_aggiuntivo = int(input("Inserisci il costo aggiuntivo "))
            posto1 = PostoStandard(numero, fila, costo_aggiuntivo)



        teatro.add_posto(posto)

print("Lista posti : ")
print(teatro.stampa_posti())


numero_prenotazione = int(input("Inserisci il numero del posto "))
fila_prenotazione = input("Inserisci la fila del posto: ").strip()

teatro.prenota(numero_prenotazione,fila_prenotazione)






    
        
        
                  

    