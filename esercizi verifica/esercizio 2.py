class Collezione:
    def __init__(self):
        self.__collezione=[]

    def get_collezione(self):
        return self.__collezione

    def aggiungi(self,dato):
        self.__collezione.append(dato)

    def unici(self):
        count ={}
        for dato in self.get_collezione():
            if dato in count:
                count[dato]+=1
            else:
                count[dato]=1

        for dato, ripeti in count.items():
            if ripeti == 1:
                print("Elemento unico", dato)


collezione=Collezione()
while True:
    x=input("Inserisci stringa : ")
    if x == "esci":
        break

    collezione.aggiungi(x)
    print(collezione.unici())