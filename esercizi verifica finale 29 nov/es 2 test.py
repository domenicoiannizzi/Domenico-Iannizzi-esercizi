'''Esercizio 2: ML
Caricamento del dataset:
Importa il dataset Iris utilizzando from sklearn.datasets import load_iris.
Esplora brevemente i dati per capire le caratteristiche e le target.
Preprocessing dei dati:
Dividi i dati in set di addestramento e di test utilizzando train_test_split di scikit-learn (ad esempio, 70% training e 30% test).
Costruzione del modello:
Scegli un algoritmo di classificazione (ad esempio, K-Nearest Neighbors, Decision Tree, Support Vector Machine).
Addestra il modello utilizzando il set di training.
Valutazione del modello:
Predici le specie nel set di test.
Valuta le prestazioni del modello utilizzando metriche come accuratezza, precisione, richiamo e la matrice di confusione.
Visualizzazione dei risultati:
In fine crea grafici per visualizzare i risultati (ad esempio, plot della matrice di confusione)'''

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,StratifiedKFold,RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from scipy.stats import randint

class IrisClassifier:
    def __init__(self, test_size=0.3, random_state=42):
        self.test_size = test_size
        self.random_state = random_state
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.iris = load_iris()
        self.X = self.iris.data
        self.y = self.iris.target


    def esplorazione(self):
        print(f"Nome delle caratteristiche: {self.iris.feature_names}")
        print(f"Target (specie): {self.iris.target_names}")
        print(f"Dimensione del dataset: {self.X.shape}")

    def divisione_dati(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=self.test_size,random_state=42)

    def pipeline(self):
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('knn', KNeighborsClassifier())
        ])
        param_dist = {
            'knn__n_neighbors': randint(1, 10),
            'knn__metric': ['euclidean', 'manhattan', 'minkowski']
        }
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=self.random_state)
    
        random_search = RandomizedSearchCV(
            pipeline, param_distributions=param_dist, n_iter=10, cv=cv, random_state=self.random_state, n_jobs=-1
        )
        
        random_search.fit(self.X_train, self.y_train)

        print(f"Migliori iperparametri: {random_search.best_params_}")
        
        self.best = random_search.best_estimator_
        print(f"Miglior modello: {self.model}")

    def valutazione(self):
            y_pred = self.best.predict(self.X_test)
            print(classification_report(self.y_test, y_pred))

            cm = confusion_matrix(self.y_test, y_pred)
            plt.figure(figsize=(6,4))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=self.iris.target_names,
            yticklabels=self.iris.target_names)

            plt.show()
    

iris=IrisClassifier()
iris.esplorazione()
iris.divisione_dati()
iris.pipeline()
iris.valutazione()