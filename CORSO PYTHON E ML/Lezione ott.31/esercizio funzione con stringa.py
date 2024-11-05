def palindroma(stringa):
    stringa1= ''.join(char.lower() for char in stringa if char.isalpha())

    return stringa1== stringa1[::-1]

stringa=input(" Inserisci stringa ")
print(palindroma(stringa))
if True:
    print("Palindroma")
    




