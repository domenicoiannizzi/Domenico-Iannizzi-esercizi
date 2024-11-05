#STAMPA CLASSIFICA



def stampa_classifica(lista_utenti):
    #li ordino in ordine decrescente

    for i in range(len(lista_utenti)): 
        for j in range(0,len(lista_utenti)-1-i):
            if lista_utenti[j].punteggio < lista_utenti[j+1].punteggio: 
                #scambio di posizione se l'ogggetto successivo è maggiore

                lista_utenti[j],lista_utenti[j+1]= lista_utenti[j+1],lista_utenti[j]  
    print("Classifica : \n")
    for x in range(1,len(lista_utenti)+1):
        print(f"{x}.Nome : {lista_utenti[x].username} - Punteggio : {lista_utenti[x].punteggio}")

(stampa_classifica(lista_utenti))