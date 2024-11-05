
import random as rand

def indovina(y):
    while True:
        numero=int(input("Inserisci il numero da indovinare :  "))
        if y > numero:
            print("Il numero è più alto")
            risposta = input("Vuoi uscire ?: ")
            if risposta == "si" :
                break
            else:
                continue
        elif y < numero:
            print("Il numero è più basso")
            risposta= input("Vuoi uscire ?: ")
            if risposta == "si" :
                continue
        else:
            print("Hai indovinato il numero!")
            break


x=int(rand.randrange(1,101))
print(indovina(x))