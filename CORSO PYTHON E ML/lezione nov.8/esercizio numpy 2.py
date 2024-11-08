import numpy as np

class SliceArray:
    def __init__(self,len,x,y):
        self.array= np.random.randint(x,y,len)

    def primi10(self):
        arr1=self.array[:10]
        return arr1
    
    def ultimi5(self):
        arr2=self.array[-5:]
        return arr2
    
    def from5to15(self):
        arr3=self.array[5:15]
        return arr3
    
    def ogni_terzo(self):
        arr4=self.array[0:20:3]
        return arr4

    def modifica(self):
        self.array[5:10] = 99
        return self.array[5:10]
       

    def stampa(self):
        print("Array completo:", self.array)
        print("Primi 10 elementi:", self.primi10())
        print("Ultimi 5 elementi:", self.ultimi5())
        print("Elementi dall'indice 5 al 15 :", self.from5to15())
        print("Ogni terzo elemento:", self.ogni_terzo())
        print("Array da 5 a 10 modificato : ", self.modifica())

array=SliceArray(20,10,50)
array.stampa()

