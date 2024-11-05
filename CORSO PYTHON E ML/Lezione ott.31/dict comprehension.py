#sintassi della dict comprehension

#dizionario={key:value for key,value in dict.items())
dict={"a":1, "b":2, "c":3}

diz={k:v * 2 for k,v in dict.items()}

print(diz)