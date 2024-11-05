#esercizio lista e dizionario

''' num=int(input("Inserisci un numero: "))
stringa= input("Inserisci una stringa: ")
booleano=bool(input("Inserisci un booleano: "))
lista=[]
lista.append(num)
lista.append(stringa)
lista.append(booleano)

print(lista)
dizio={"tipididato": lista}
       
print(dizio)'''

##############################################

#esempi con i set

'''set1={1,2,3,4,5}
set2={1,2,25,67,78,4}

set3= set1 &set2
print(set3) # intersezione

set4=set1 | set2 
print(set4) #unione

set5= set1- set2
print(set5)        #difference: gli elementi di 1 non contenuti in 2

set6= set2- set1
print(set6)      #difference: viceversa

set1.add(29)
print(set1)
set1.remove(1)
print(len(set1))'''



##############################################################

'''num=int(input("Inserisci un numero:  "))
if num %2==0:
  print("Il numero è pari")
else:
  print("Il numero è dispari")

oppure anche

if num % 2:
  print("Il numero è dispari")
else:
  print("Il numero è pari")'''

##################################################################

'''anno=int(input("Inserisci anno: "))
if (anno % 4==0 and anno %100 !=0) or (anno%400==0):
  print("L'anno è bisestile")
else:
  print("L'anno non è bisestile")'''

#################################################################

'''username="admin"
password="1234"

username1=input("Inserisci username: ")
password1=input("Inserisci password: ")

if username1==username and password1==password:
  print("Successful login")
else:
  print("Wrong username or password")'''
  
#################################################################
'''username="admin"
password="1234"

username1=input("Inserisci username: ")
password1=input("Inserisci password: ")

if username1==username and password1==password:

 
  scelta=bool(int(input("Inserisci scelta effettuata : ")))
  risposta="si"
  
  if scelta==0
    domanda=input("Inserisci colore preferito: ")
    risposta1=input("Vuoi cambiare password? ")
    if risposta == risposta1:
      stringa=input(" inserisci colore preferito: ")
      stringa1=input("Inserisci nuova password")
    else:
      print("Ok, non vuoi cambiare password")
      

  else:
    domanda2=input("Inserisci animale preferito: ")
    risposta2=input("Vuoi cambiare password? ")
    if risposta== risposta2:
      stringa=input(" inserisci animale preferito: ")
      stringa1=input("Inserisci nuova password")
    else:
      print("Ok, non vuoi cambiare password")

else:
  print("Wrong username or password")'''


#########################################################################
##########################################################################

lista_acquisti=[]
lista_articoli=["Nike Air Force 1","Adidas Stan Smith", "Jordan 1","Jordan 4", "Alexander McQueen", "Nike Air Max", "Timberland", "Adidas Samba"]

#lista possibilità utente e admin
lista_poss_utente=["aggiungere a lista acquisti o rimuovere da lista acquisti", "visualizzare lista articoli"]
lista_poss_admin=["Aggiungere a lista articoli", "Rimuovere da lista articoli"]

#credenziali utente
admin_usr="admin"
admin_psw= "psw"

#Login
scelta=bool(int(input("Inserisci scelta effettuata: 0 per user, 1 per admin:    ")))

if scelta==0: 

  #registrazione utente e login
  nome_utente= input("Inserisci nome utente per la registrazione: ")
  password=input("Inserisci password per la registrazione: ")
  
  username=input("Inserisci Username :  ")
  password1=input("Inserisci Password:  ")
  if username== nome_utente and password1== password:
    print("Login effettuato")
    cosa_fare= input("Scegli cosa fare da lista possibilità utente: aggiungere/rimuovere o visualizzare  articoli da lista articoli:          ")
    if cosa_fare==lista_poss_utente[0] :
       lista_acquisti.append("Nike Air Force 1", "Adidas Stan Smith", "Jordan 1")
       lista_acquisti.remove("Jordan 1") 
       print(lista_acquisti)
    
    else:
       print(lista_articoli)

  else:
    print("Login non effettuato correttamente")

else:
  username=input("Inserisci Username :  ")
  password1=input("Inserisci Password:  ")
  if username== admin_usr and password1 == admin_psw:
    print("Login effettuato")
    cosa_fare1= input("Scegli cosa fare da lista possibilità admin: aggiungere o rimuovere articoli da lista articoli   " )
    if cosa_fare1 == lista_poss_admin[0]:
      lista_articoli.append("Lelly Kelly")
      print(lista_articoli)

    else:
      lista_articoli.remove("Jordan 4")
      print(lista_articoli)
    
  else:
    print("Login non effettuato correttamente")
  