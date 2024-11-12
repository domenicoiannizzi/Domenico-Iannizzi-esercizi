# #con modo read, se non esiste errore

# with open("prova.txt","r") as file:
#     s1=file.read()

#     s1=file.readlines() #legge le righe
#     s1=file.readline() #stampa la prima riga


# #con modo write.

# with open("prova.txt","w") as file: 
#     s1=file.write("ciao")  #crea il file con ciao se non esiste, se esiste sovrascrive il contenuto

# print(s1)


# #con modo append:

# with open("prova.txt","a") as file: 
#     s1=file.append("asa")    #crea o aggiunge


###############################################################################################################################################

# ho un file csv con righe e colonne.per ottenere la prima colonna:
# righe= s1.split("\n")
# for riga in righe:
#     elementi=riga.split(',')
#     print(elementi[0])  

# posso saltare indentazione con lo slicing: for riga in righe [1:]


######################################################################################################################################à
#mi faccio stampare le righe:

# mi creo la lista:
# matrice=[0]
#  righe= s1.split("\n")
# # for riga in righe[1:]:
# #     elementi=riga.split(',')
# #     matrice.append(lementi)

# print(matrice)


######################################################################################################################################
# FILE BINARIO:

# with open("prova2", "wb") as file: ----> devo trasformare il dato anzichè in stringa, in binario. 

# import pickle

# diz={"uno":"due"}

# with open("prova2.pkl","wb") as file:
#     #pickle.dump(diz,file)

# with open("prova2.pkl","rb") as file:
#    contenuto=pickle.load(file)

# print((contenuto)) 