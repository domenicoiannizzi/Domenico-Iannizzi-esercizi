# Carica il dataset "Digits" utilizzando sklearn.datasets.load_digits().
# Esplora i dati per comprendere la struttura delle immagini e le etichette associate.
# Applica PCA per ridurre i dati da 64 dimensioni (8x8 pixel) a 2 dimensioni.
# Visualizza i dati nel nuovo spazio bidimensionale, colorando i punti in base alla cifra rappresentata.
# Suddividi il dataset originale in set di training e test.
# Addestra un modello di classificazione (ad esempio, LogisticRegression o SVC) sui dati originali e calcola l'accuratezza sul test set.
# Ripeti l'addestramento del modello utilizzando i dati ridotti con PCA e confronta le prestazioni.
# Analizza come la riduzione della dimensionalità influisce sulla capacità del modello di classificare correttamente le cifre.

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

# Inizializzazione del dataset Wine
digits_data = load_digits()
X = digits_data.data  # Caratteristiche
y = digits_data.target  # Etichette


# Esplora i dati
print(f"Shape dei dati originali: {X.shape}")
print(f"Etichette disponibili: {np.unique(y)}")
plt.figure(figsize=(10, 5))

for i in range(1, 11):
    plt.subplot(2, 5, i)
    plt.imshow(digits_data.images[i], cmap='gray')
    plt.title(f"Label: {digits_data.target[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()



#Applicazione PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f"Shape dei dati ridimensionati: {X_pca.shape}")

# Visualizza i dati nel nuovo spazio bidimensionale
dfpca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
dfpca['pca'] = y


plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=15)
plt.colorbar(scatter, label='Cifre')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.title('Digits dataset dopo PCA (2D)')
plt.show()




# Split del dataset in addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creazione del modello con dati originali
modello = LogisticRegression(max_iter=1000, solver='lbfgs')

# Addestramento del modello con dati originali
modello.fit(X_train, y_train)

# Valuto l'accuratezza del modello originale sul set di training
previsioni = modello.predict(X_test)
accuratezza_train = accuracy_score(y_test, previsioni)


# Split del dataset in addestramento e test Pca
X_pca_train, X_pca_test, y_pca_train, y_pca_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

#Creazione del modello con dati ridotti
modello_pca = LogisticRegression(max_iter=1000, solver='lbfgs')

# Addestramento del modello
modello_pca.fit(X_pca_train, y_pca_train)

# Valuto l'accuratezza del modello con dati ridotti sul set di training
previsioni_pca = modello_pca.predict(X_pca_test)
accuratezza_train_pca = accuracy_score(y_pca_test, previsioni_pca)


print("Accuratezza del modello originale: ",accuratezza_train)
print("Accuratezza del modello con PCA: ", accuratezza_train_pca)