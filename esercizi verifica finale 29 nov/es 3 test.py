'''Descrizione: Crea un dataset autogenerandolo monolineare con 50 posizioni matematica e cambia la sua forma 
in 10 file da 5, normalizza i valori e rendili interi , nessun valore deve essere uguale a un altro sulla stessa linea 
della collezione  dopodiché stampa un grafico che lo rappresenti. '''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generazione del dataset
arr=np.random.uniform(1, 25, size=50)
arr1=arr.reshape(10,5)

df = pd.DataFrame(arr1, columns=[f"Colonna{i+1}" for i in range(5)])

#conversione in interi
df = df.astype(int)

print(df.nunique())

def trova_e_rimuovi(df):
    for col in df.columns:
        if df[col].duplicated().any():  
            print(f"Colonna '{col}' ha valori duplicati.")
            df = df.drop(columns=[col])  
            return df, col  
    print("Non ci sono duplicati nelle colonne.")
    return df, None  

df1, colonna = trova_e_rimuovi(df)

if colonna:
    print(f"Colonna rimossa: {colonna}")
else:
    print("Nessuna colonna è stata rimossa.")


plt.figure(figsize=(8, 6))

for col in df1.columns:  
    plt.scatter(df1.index, df1[col], label=col)
    plt.show()
    plt.title('Distribuzione dei valori delle righe e colonne')
    plt.xlabel('Riga')
    plt.legend()
    plt.ylabel('Colonna')
