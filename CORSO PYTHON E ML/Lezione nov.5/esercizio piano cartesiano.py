class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi_punto(self, dx1, dy1):
        self.x += dx1
        self.y += dy1

    def distanza_da_origine(self):
        
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        #Restituisce una rappresentazione stringa del punto
        return f"Punto({self.x}, {self.y})"

class PianoCartesiano:
    def __init__(self):
        self.punti = []

    def aggiungi_punto(self, x, y):

        punto = Punto(x, y)
        self.punti.append(punto)

    def stampa_piano(self):
           return self.punti if len(self.punti) > 1:

    def muovi_punti(self, dx1, dy1):
        for punto in self.punti:
            punto.muovi_punto(dx1, dy1)

    def distanza_or(self):
        return [punto.distanza_da_origine() for punto in self.punti]


piano = PianoCartesiano()


piano.aggiungi_punto(4, 5)
piano.aggiungi_punto(1, 2)


print(piano.stampa_piano())


piano.muovi_punti(2, 3)
print("Dopo muovi punto : \n",piano.stampa_piano())

piano.distanza_or()
distanze = piano.distanza_or()
for i, distanza in enumerate(distanze):
    print(f"Distanza del Punto {i+1} dall'origine: {distanza}")

