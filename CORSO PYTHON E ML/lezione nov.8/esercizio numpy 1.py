import numpy as np

class CalcolaArray:
    def __init__(self, x, y):
        self.array = np.arange(x, y)

    def stampa_tipo(self):
        return self.array.dtype

    def cambia_tipo(self, nuovotipo):
        self.array = self.array.astype(nuovotipo)

    def stampa_forma(self):
        return self.array.shape


array = CalcolaArray(10, 50)

print(array.stampa_tipo())

array.cambia_tipo(np.float64)


print(array.stampa_tipo())

print(array.stampa_forma())