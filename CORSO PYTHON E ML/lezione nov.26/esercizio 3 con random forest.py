from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carico il dataset iris
wine= load_wine()
X = wine.data
y=wine.target

#creazione del dataframe
df=pd.DataFrame(X, columns=wine.feature_names)
df['classi']=y

# print(df.head())
# print(df.tail())

#Esplora il dataset
print(df.describe())
print(df['classi'].value_counts())

sns.countplot(x='classi', data=df)
plt.title('Distribuzione delle classi')
plt.show()

#Dividi i dati in due set: l'80% per il training e il 20% per il test.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#dati di test e train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#modello random forest
model = RandomForestClassifier()
model.fit(X_train, y_train)


