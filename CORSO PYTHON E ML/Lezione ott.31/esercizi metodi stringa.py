stringa="Ciao"

# #print(stringa.startswith("i")) o endswith

# numero=input("Inserisci un numero")
# if numero.isdecimal():  #verifica caratteri decimali, isdigit numerici
#     print("Ok")

# else:
#     print("No")

# print (stringa.isalnum()) #verifica caratteri alfanumerici, isalpha alfabetici
# #upper in maiuscolo, lower in minuscolo

print(stringa.count("o")) #count della lettera

stringa1=stringa.replace("Ciao", "ciao a qualcuno") #rimpiazza

lista=stringa.split(',')  #split riporta in una lista
print(lista)

stringa2=''.join(lista) # ' '. join riporta la stringa dalla lista
print(stringa2)
