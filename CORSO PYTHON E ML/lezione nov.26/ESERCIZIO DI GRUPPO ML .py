"""Creare un modello di classificazione avanzato
 utilizzando il dataset "Wine" di scikit-learn.
 Il modello dovrà:
 Pre-elaborare i dati con scaling standard.
 Ridurre la dimensionalità con PCA per
 migliorare l'efficienza computazionale.
 Utilizzare un modello di Gradient Boosting
 Classifier.
 Ottimizzare gli iperparametri con
 RandomizedSearchCV.
 Valutare le prestazioni utilizzando
 StratifiedKFold per mantenere la proporzione
 delle classi."""

import numpy as np
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

# Inizializzazione del dataset Wine
wine_data = load_wine()
X = wine_data.data  # Caratteristiche
y = wine_data.target  # Etichette

# Standardizzazione delle caratteristiche utilizzando la classe StandardScaler per portare tutte le feature su una scala comune
scaler = StandardScaler()

# Riduzione della dimensionalità
pca = PCA()

# Utilizzo modello con algoritmo GradientBoostingClassifier
modello = GradientBoostingClassifier()

# Pipeline
pipeline = Pipeline([ 
    ('scaler', scaler), 
    ('pca', pca), 
    ('modello', modello)
])

# Definizione della distribuzione degli iperparametri
param_dist = {
    'pca__n_components': sp_randint(5, 13),  # Variabilità nel numero di componenti PCA
    'modello__n_estimators': sp_randint(50, 200),  # Numero di stime
    'modello__learning_rate': uniform(0.01, 0.2),  # Tasso di apprendimento
    'modello__max_depth': sp_randint(1, 5),  # Profondità massima degli alberi
    'modello__subsample': uniform(0.6, 0.4),  # Subcampionamento
    'modello__min_samples_split': sp_randint(2, 10),  # Campioni minimi per dividere
    'modello__min_samples_leaf': sp_randint(1, 10),  # Campioni minimi per foglia
    'modello__max_features': ['sqrt', 'log2', None]  # Numero massimo di feature da considerare (auto non valido)
}

# Definizione della Cross Validation
cross_validation = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Ottimizzazione degli iperparametri
random_search = RandomizedSearchCV(pipeline, param_distributions=param_dist, n_iter=50, cv=cross_validation, scoring='accuracy', random_state=42, n_jobs=-1)

# Split del dataset in addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Addestramento del modello con RandomizedSearchCV
random_search.fit(X_train, y_train)

# Utilizza il miglior modello trovato
miglior_modello = random_search.best_estimator_
miglior_punteggio = random_search.best_score_

# Stampa del miglior modello e del miglior punteggio
print("Prestazione del miglior modello: ")
print(miglior_modello)

print("Il miglior punteggio: ")
print(miglior_punteggio)

# Predizioni sui dati di addestramento e di test
train_accuracy = random_search.score(X_train, y_train)
test_accuracy = random_search.score(X_test, y_test)

# Stampa l'accuratezza sui dati di addestramento e test
print(f"Accuratezza su Training Set: {train_accuracy}")
print(f"Accuratezza su Test Set: {test_accuracy}")

# Predizioni finali sui dati di test
y_pred = miglior_modello.predict(X_test)

# Report delle prestazioni
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Matrice di confusione
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Accuratezza finale
print("Accuratezza finale:")
print(accuracy_score(y_test, y_pred))
