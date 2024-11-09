import numpy as np

class SliceArray:
    def __init__(self,len,x,y):
        self.array= np.random.randint(x,y,len)

    def primi10(self,n):
        arr1=self.array[:n]
        return arr1
    
    def ultimi5(self,n):
        arr2=self.array[-n:]
        return arr2
    
    def from5to15(self,x,y):
        arr3=self.array[x:y]
        return arr3
    
    def ogni_terzo(self,x,y,step):
        arr4=self.array[x:y:step]
        return arr4

    def modifica(self,x,y,val):
        self.array[x:y] = val
        return self.array
       

    def stampa(self):
        print("Array completo:", self.array)

array=SliceArray(20,10,50)
print(array.array)

while True:
        print("--- menù---")
        print("1. Primi N elementi")
        print("2. Ultimi N elementi")
        print("3. Elementi dall'indice x ad y")
        print("4. Ogni x elemento")
        print("5. Stampa l'array modificato da x a y con valore val")

        scelta = input("Scegli un'opzione : ")


        if scelta == '1':
            print("\n Primi N elementi:", array.primi10(4))
        elif scelta == '2':
            print("\nUltimi N elementi:", array.ultimi5(6))
        elif scelta == '3':
            print("\n Elementi dall'indice x ad y:", array.from5to15(1,6))
        elif scelta == '4':
            print("\n Ogni x elemento:", array.ogni_terzo(2,12,2))
        elif scelta == '5':
            print("\n Array modificato :",array.modifica(4,9,15))
            array.stampa()
        else :
            print("Esci dal programma.")
            break 