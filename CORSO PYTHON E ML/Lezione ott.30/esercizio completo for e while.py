#punto 1
while True:
    n=int(input("Inserisci un numero "))
    if n <=0 :
        continue
    else:
        break

#punto2 e 3

lista_pari=[]
lista_dispari=[]

for x in range(1,n+1):
    if x % 2==0:
        lista_pari.append(x)
    else:
        lista_dispari.append(x)

print("La lista pari : ", lista_pari)
print("La lista dispari :",lista_dispari)

somma=0
for i in lista_pari:
    somma=somma+i

print("somma pari", somma)

sum=0
for k in lista_dispari:
    sum=sum+k

print("Somma dispari",sum)

#punto4

for i in range(2, n):
    if n % i !=0:
        print(f"{n} è un numero primo")
        break

    else:
        print(f"{n} non è primo")

