class Punto():
    def __init__(self,x,y):
        self.x= x
        self.y=y
    def muovi_punto(self,dx1,dy1):
        self.x += dx1
        self.y += dy1


    def distanza_da_origine(self):
        print("Distanza da origine è :", self.x**2 + self.y**2)

puntos = Punto(3, 4)
puntos.muovi_punto(1, 5)
print(puntos.distanza_da_origine())





       
        