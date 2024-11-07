from abc import ABC, abstractmethod
class Cemento(ABC):
   @abstractmethod
   def strumento(self):
      return
    
class Cavo(ABC):
    @abstractmethod
    def strumento(self):
        pass

class Operaio(ABC):
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    @abstractmethod
    def lavora(self):
        pass

class Muratore(Operaio,Cemento):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def strumento(self):
        return f"{self.nome} ha bisogno di cement "
    
    def lavora(self):
        return f"{self.nome} sta lavorando come muratore."
    
class Elettricista(Operaio,Cavo):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def strumento(self):
        return f"{self.nome} usa il cavo."

    def lavora(self):
        return f"{self.nome} sta lavorando come elettricista."



muratore = Muratore("marco", 21)
elettricista = Elettricista("giovanni", 28)

print(muratore.lavora())
print(muratore.strumento())
print(elettricista.lavora())
print(elettricista.strumento())
