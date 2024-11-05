#Sequenza di Fibonacci fino a N Descrizione: Chiedi all'utente di inserire un numero N. 
# Il programma dovrebbe stampare la sequenza di Fibonacci fino a N. 
# Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100.

def domanda_numero():
    numero=int(input("inserisci numero :  "))
    return numero 

def sequenza(numero):
    fibonacci=[]
    primo=0
    secondo=1
    for x in range (numero+1):
        fibonacci.append(primo)
        primo,secondo= secondo,primo+secondo
    return fibonacci

numero=int(input("Inserisci un numero:  "))
print(sequenza(numero))