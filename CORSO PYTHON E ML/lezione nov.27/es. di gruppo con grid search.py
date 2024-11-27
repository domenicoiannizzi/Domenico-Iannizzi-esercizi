# Carica il dataset "Wine" utilizzando sklearn.datasets.load_wine().
# Esplora i dati per comprendere le caratteristiche e le classi presenti.
# Suddividi il dataset in set di training e test.
# Crea un modello di classificazione utilizzando RandomForestClassifier.
# Definisci una griglia di iperparametri, ad esempio variando il numero di stimatori (n_estimators), la profondità massima (max_depth) e il criterio di qualità dello split (criterion).
# Utilizza GridSearchCV per trovare la migliore combinazione di iperparametri, utilizzando una validazione incrociata con 5 fold.
# Dopo aver trovato i migliori iperparametri, addestra il modello ottimizzato sull'intero set di training.
# Valuta le prestazioni del modello sul test set utilizzando metriche come l'accuratezza, la precisione, il richiamo e l'F1-score.
# Visualizza la matrice di confusione per analizzare in dettaglio le prestazioni del modello.
# Discuta i risultati e l'importanza delle diverse caratteristiche nel modello finale.



from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

# Inizializzazione del dataset Wine
wine_data = load_wine()
X = wine_data.data  # Caratteristiche
y = wine_data.target  # Etichette


# Esplora i dati
print(f"Caratteristiche dataset: {wine_data.feature_names}")
print(f"Classi di vino disponibili: {wine_data.target_names}")


print("Dimensione x: ",X.shape, "Dimensione y: ",y.shape)



# Split del dataset in addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Creazione del modello
modello = RandomForestClassifier(random_state=42)


#Parametri per gridsearch
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None],
    'criterion': ['gini', 'entropy']
}


#Configurazione GridSearch
grid_search_cv = GridSearchCV(
    estimator=modello,
    param_grid=param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=-1
)


#Addestramento del modello
grid_search_cv.fit(X_train, y_train)


#Visualizzazione miglior parametri
print(f"Migliori iperparametri: {grid_search_cv.best_params_}")

#Miglior modello ottenuto e addestramento
bestrf = grid_search_cv.best_estimator_

bestrf.fit(X_train, y_train)

#Predizione sull'etichetta
y_pred = bestrf.predict(X_test)


#Classificazione delle prestazioni
classificazione = classification_report(y_test, y_pred)
print("Classificazione del modello: \n", classificazione)


# Matrice di confusione
matrice_confusione = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(matrice_confusione, annot=True, fmt='d', cmap='Blues',
            xticklabels=wine_data.target_names,
            yticklabels=wine_data.target_names)

plt.show()




#Analisi dell'importanza delle caratteristiche
importances = bestrf.feature_importances_
indices = np.argsort(importances)[::-1]

#Visualizziamo l'importanza delle caratteristiche
plt.figure(figsize=(10, 6))
plt.title("Importanza delle caratteristiche")
plt.barh(range(X.shape[1]), importances[indices], align="center")
plt.yticks(range(X.shape[1]), np.array(wine_data.feature_names)[indices])
plt.xlabel("Importanza")
plt.show()



#Validazione incrociata sul modello ottimizzato
cross_val_scores = cross_val_score(bestrf, X, y, cv=5, scoring='accuracy')
print(f"Accuratezza media dalla validazione incrociata: {np.mean(cross_val_scores):.4f}")