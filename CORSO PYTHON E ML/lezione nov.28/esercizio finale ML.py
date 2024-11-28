'''Obiettivo: Creare un modello di Machine Learning per classificare le cifre da 0 a 9 utilizzando il
dataset MNIST Digits.

Punti dell'esercizio

Importazione dei Dati
Carica il dataset MNIST Digits utilizzando sklearn.datasets.
Visualizza alcune cifre per comprendere i dati.

Preprocessing dei Dati
Normalizza i dati dividendo i valori dei pixel per il massimo valore possibile (16).
Dividi il dataset in un training set e un test set usando train_test_split.

Scelta del Modello
Scegli un algoritmo di classificazione, come Support Vector Machine (SVM) o Random Forest.
Configura il modello con parametri di base.
Addestramento del Modello
Addestra il modello sui dati di training.
Verifica che il processo termini senza errori.

Valutazione del Modello
Utilizza il test set per valutare il modello.
Calcola l'accuratezza e stampa un report di classificazione.

Visualizzazione dei Risultati
Mostra alcune immagini del test set con le loro predizioni e i valori reali.
Identifica eventuali errori di classificazione.

Esperimenti Extra (Facoltativo)
Cambia il modello con un altro algoritmo (es. k-Nearest Neighbors o Decision Tree).
Applica la cross-validation per migliorare la stabilità delle valutazioni.
Genera una matrice di confusione per analizzare gli errori.'''


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import  train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score

#carica dataset
digits=load_digits()
X=digits.data
y=digits.target

#visualizzo i dati
print(f"Caratteristiche dataset: {digits.feature_names}")
print(f"Target: {digits.target_names}")
print("Dimensione x: ",X.shape, "Dimensione y: ",y.shape)

for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(digits.images[i], cmap='viridis')
    plt.title(f"Label: {digits.target[i]}")
plt.tight_layout()
plt.show()

#X normalizzati
X_norm= X / 16
print("Dimensione x: ",X.shape, "Dimensione y: ",y.shape)

#dividi in dati di training e test
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=42)

#modello random forest

rf=RandomForestClassifier(random_state=42)

#randomized search

param_dist = {
    'n_estimators': [50, 100, 200], 
    'max_depth': [None, 10, 20, 30],  
    'min_samples_split': [2, 5, 10],  
    'min_samples_leaf': [1, 2, 4]  
}
 

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42) 

random_search = RandomizedSearchCV(
    estimator=rf, 
    param_distributions=param_dist, 
    n_iter=10,  
    cv=cv,  
    scoring='accuracy', 
    random_state=42,
    verbose=1,
    n_jobs=-1  
)

random_search.fit(X_train, y_train)

#migliori iperparametri
print(f"Migliori iperparametri: {random_search.best_params_}")

#modello migliore

best_rf = random_search.best_estimator_
y_pred = best_rf.predict(X_test)

#valutazione con classification report e matrice di confusione

cr=classification_report(y_test, y_pred)
print("Classification Report:\n", cr)

acc=accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2f}")


matrice_confusione = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(matrice_confusione, annot=True, fmt='d', cmap='Blues',
            xticklabels=digits.target_names,
            yticklabels=digits.target_names)

plt.show()

#errori di classificazione

def errori_classificazione(y_test, y_pred):
    lista_errori= [i for i in range(len(y_test)) if y_test[i] != y_pred[i]]
    return lista_errori 

errori=errori_classificazione(y_test, y_pred)
print(len(errori))
if errori:
    for i in errori[:10]:
        print("Predizione: ", y_pred[i], "Reali: ", y_test[i])

else:
    print("Nessun errore di classificazione trovato!")

#visualizzazione errori di classificazione
# if errori:
#         for i in range(10):
#             plt.subplot(2, 5, i+1)
#             plt.imshow(X_test[i].reshape(8,8), cmap='viridis')
#             plt.title(f"Pred: {y_pred[i]}\nReal: {y_test[i]}")
#             plt.tight_layout()
#             plt.show()

#cross_validation_score
cross_val_score = cross_val_score(best_rf, X_norm, y, cv=5, scoring='accuracy')
print(f"Accuratezza media dalla validazione incrociata: {np.mean(cross_val_score):.2f}")



    