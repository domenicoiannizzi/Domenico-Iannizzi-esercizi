#Parte 1

#Inserisci numero e verifica se è pari o dispari

# numero= int(input("Inserisci un numero : "))
# if numero %2 == 0:
#     print("Il numero è pari")
# else:
#     print("Il numero è dispari")

# #Parte 2

# #Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da n a 0 (compreso), decrementando di 1.
# # Deve potersi ripete all’infinito

# while True:
#     numero1= int(input("Inserisci il numero : "))
#     if numero > 0:
#        for x in range(numero1,-1,-1):
#            print("Il numero é :", x)

#     else:
#         print("Il numero è negativo")

#Parte 3
#Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero nella lista.


# lista=[4,5,6,7,8]
# for x in lista:
#     print(f"Il quadrato del numero  {x} é : " , x**2)


#Parte 4

#punto 1
#Il sistema deve:
#Utilizzare un ciclo for per trovare il numero massimo nella lista.

# lista=[4,5,6,7,8]
# massimo= lista[0]
# for x in lista:
#     if x > massimo:
#         massimo = x

# print("Il massimo della lista è :  ", massimo)

# # #punto2

# # #Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.


# count=0
# while i < len(lista):
#     i=i+1
#     count=count+1

# print("Gli elementi contenuti sono :  ",count )

#punto3

#Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
# altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.

lista1=[5,"cavallo",12,"cane",1,16,18]
if len(lista1)==0:
    print("La lista è vuota")
else:
   lista_num=[]
   lista_par=[]
   lista_num=[num for num in lista1 if type(num) in (int,float)]
   lista_par=[word for word in lista1 if type(word) is str]

print("Lista numeri: ", lista_num)
print("Lista parole: ", lista_par)

#Trovare massimo della lista
lista_num.sort(reverse=True)
print("Il massimo è : ",lista_num[0])
massimo= max(lista_par)
print(massimo)

#     





