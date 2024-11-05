# frutta=["mela", "banana","lampone", "ciliegia"]

# frutta1=[frutto for frutto in frutta if "o" in frutto]
# print(frutta1)

# #corrisponde a :

# for frutto in frutta:
#     if "o" in frutta1:
#         ecc


#################################################################################

lista=[1,2,3,4,5,6]
lista_Pari=[]

#classico for per inserire i pari:
#ecc...

#faccio list comprehension:

lista_pari2=[num for num in lista if num %2==0]

