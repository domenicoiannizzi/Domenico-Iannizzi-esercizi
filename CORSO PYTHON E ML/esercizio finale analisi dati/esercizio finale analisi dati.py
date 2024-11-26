import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#array e dataframe
num_giorni = 365
media_visit=1200
dev_std=900

visite=np.random.normal(loc=media_visit,scale= dev_std,size=num_giorni)
trend=np.random.normal(-150,150,365)

visite_giornaliere=[max(x,0) for x in visite * trend]

lista_pat=['cuore','ossa','testa']
patologie=np.random.choice(lista_pat,365)

date = pd.date_range(start="2022-01-01", periods=365)

df=pd.DataFrame({'visitatori': visite_giornaliere,
                  "Patologia": patologie},
                  index=date)

df['visitatori'] = df['visitatori'].astype(int)

#analisi dati
# while True:
#         print("\n--- Menu ---")
#         print("1. Numero medio visitatori per mese e deviazione standard")
#         print("2. Patologia più frequente nel dataframe e patologie meno frequente")
#         print("3. Giorno con più visitatori e giorno con meno visitatori")
#         print("4 Esci")
#         scelta = input("Scegli un'opzione: ").strip()

#         if scelta == "1":
#                 mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
#                 x=input("Vuoi scegliere un mese o vuoi la media per tutti i mesi? ").strip()
#                 if x == "si":
#                    scelta1=input("Inserisci mese:  ")
#                    if scelta1.lower() in mesi:
#                           num_mesi = mesi.index(scelta1) + 1
#                           mesi_group = df.groupby(df.index.month)['visitatori']
#                           media_visit = mesi_group.get_group(num_mesi).mean()
#                           dev_std = mesi_group.get_group(num_mesi).std()
#                           print(f"\nIl numero medio di visitatori nel mese di {scelta1} è {media_visit:.2f} con una deviazione standard di {dev_std:.2f}")

#                    else:
#                           print("Scelta errata")

              
#                 elif x == "no":
            
#                         mesi_group= df.groupby(df.index.month)['visitatori']
#                         for i, mese in enumerate(mesi):
#                                 media_visit = mesi_group.get_group(i+1).mean()
#                                 dev_std = mesi_group.get_group(i+1).std()
#                                 print(f"\n Il numero medio di visitatori nel mese di {mese} è {media_visit:.2f} con una deviazione standard di {dev_std:.2f}")
#                 else:
#                  print("Scelta non valida. Riprova.")                
#         elif scelta == "2":
#               patologia_count= df['Patologia'].value_counts()
#               print("Patologia più frequente : ",patologia_count.idxmax())
#               print("Patologia non valida : ",patologia_count.idxmin())

#         elif scelta == "3":
#               giorno_max = df['visitatori'].idxmax()
#               visitatori_max = df['visitatori'].min()
#               giorno_min = df['visitatori'].idxmin()
#               visitatori_min = df['visitatori'].min()
#               print("Giorno con più visitatori : ", giorno_max, " -num_visitatori ", visitatori_max)
#               print("Giorno con meno visitatori : ", giorno_min, " - num_visitatori ", visitatori_min)

#         elif scelta == "4":
#               print("Esci")
#               break
#         else:
#               print("Scelta non valida. Riprova.")

#Visualizzazione dati

#primo punto
plt.figure(figsize=(10,6))
plt.plot(df.index, df['visitatori'])
plt.title('Numero di visitatori giornalieri')
plt.xlabel('Data')
plt.ylabel('Numero di visitatori')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()

#secondo punto e terzo punto

media_mobile_7gg = df['visitatori'].rolling(window=7).mean()
media_mensile = df.groupby(df.index.month)['visitatori'].mean()

fig = plt.figure(figsize= (12, 8))
ax1 = fig.add_subplot(2,2,1)
ax1.plot(df.index,media_mobile_7gg,color='red')
ax1.set_title('Numero di visitatori giornalieri con media mobile a 7 Giorni')
ax1.set_xlabel('Data')
ax1.set_ylabel('Numero di visitatori')


mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
ax2=fig.add_subplot(2,2,2)
ax2.plot(mesi, media_mensile, color='orange')
ax2.set_title('Media Mensile dei Visitatori')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Numero Medio di Visitatori')
ax2.set_xticks(rotation=45)

plt.show()

#quarto punto

patologia_count = df['Patologia'].value_counts()
explode=[0.1,0,0]
plt.pie(patologia_count, labels=['cuore','testa','ossa'],explode=explode,autopct='%1.1f%%')
plt.title('Patologie')
plt.show()
