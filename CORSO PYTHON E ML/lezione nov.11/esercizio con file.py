from random import randint
numeri=[randint(1,100) for i in range(5)]

# for numero in numeri:
#     print(numero)
s1= ""
for numero in numeri:
    s1 += f"{numero}\n"

with open("numerirandom.txt","w") as file:
   
    file.write(s1) 

# seconda parte

lista_num=[]
with open("numerirandom.txt","r") as file:
    contenuto=file.read()
    
contenuto=contenuto.split("\n")
for numero1 in contenuto:
    if numero1.isdecimal():
        lista_num.append((numero1.strip()))

#print(lista_num)
count=0
for x in range(5):
  
    num_inserire=input("Inserisci numero : ")
    if num_inserire in lista_num:
        print(f"Hai indovinato il numero {num_inserire}")
        count+=1
        if count >=2:
            
            print("Hai indovinato almeno due numeri, perfetto")
            break

    else:
        print("Non hai indovinato")

if count<2:

    print("Gioco perso")