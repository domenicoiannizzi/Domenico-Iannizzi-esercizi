#while vuole ripetizione, regola di uscita altrimenti va all'infinito. count=count+1 esempio. Break interrompe oppure inserisco condizione



########################################################################################################################################
while True:
    risposta_utente=input(" Vuoi inserire un numero?   ")
    if risposta_utente == "si":
        numero=int(input("Inserisci un numero :  "))
        x=numero
        while x>=0:
            print("Il numero é : ", x)
            x=x-1
    else:
        print("Non inserire numero")

    ripeti=input("Vuoi inserire un numero")
    if ripeti == "si":
        break



lista_num_primi=[]
while True:
    num=int(input("Inserisci un numero :  "))
    if num > 1:  
            is_prime= True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    continue
            if is_prime:
                print("Il numero ", num, "è primo")
                lista_num_primi.append(num)
            
            if len(lista_num_primi) ==5:
                break


            






    


    





    