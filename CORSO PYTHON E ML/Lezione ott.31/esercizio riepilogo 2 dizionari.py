diz={}
num=int(input("Quanti utenti vuoi inserire? : "))
for i in range(1,num):
    nome=input(f"Inserisci nome dell' alunno num {i} : ")
    sum=0
    voti=int(input("Quanti voti vuoi inserire ? : "))
    for y in range(voti):
        voto=int(input("Inserisci voto : "))
        sum +=voto
    media= sum / voti
    diz[nome]= media
    
    

print("Dizionario: \n ", diz)

    
