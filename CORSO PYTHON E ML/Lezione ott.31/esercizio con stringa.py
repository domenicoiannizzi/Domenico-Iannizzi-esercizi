stringa=input("Inserisci una parola : "  )
stringa1=stringa.lower()

indice=0
for char in stringa1:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            print(f"La vocale è : {char} alla posizione {indice} " )
            
        indice +=1




              

