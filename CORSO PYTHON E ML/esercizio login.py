import random 

def acccesso_utente():
    username=input("Inserisci nome utente:  ")
    password=input("Inserisci password :  ")
    
possibilità=["si","no"]
x= random.choice(possibilità)
y=random.choice(possibilità)

def verifica_accesso():
    if x == "si" and y == "si":
        return True
    else:
        return False
    

def messaggio():
    if x== "si" and y=="si" :
        print("Benvenuto !")
    else :
        print("Nome utente o password errati")


print(acccesso_utente())
print(verifica_accesso())
print(messaggio())


