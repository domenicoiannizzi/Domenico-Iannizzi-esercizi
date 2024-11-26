from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.decomposition import PCA
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

# Applica PCA per ridurre a 2 componenti principali
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Crea un DataFrame per le componenti principali
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

# Grafico scatter delle componenti principali
plt.figure(figsize=(10,8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2')
plt.title('PCA del dataset wine')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.show()

#dati di test e train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#modello random forest
modello = RandomForestClassifier(random_state=42)
modello.fit(X_train, y_train)
previsioni=modello.predict(X_test)

#classification report
report = classification_report(y_test, previsioni, target_names=wine.target_names)
print("Classification Report:\n", report)


#matrice di confusione
matrice = confusion_matrix(y_test, previsioni)
sns.heatmap(matrice, annot=True,
            xticklabels=wine.target_names,
            yticklabels=wine.target_names)

plt.title('Confusion Matrix')
plt.show()

# feature importances
importances = modello.feature_importances_
indices = np.argsort(importances)[::-1]  
sns.barplot(x=[wine.feature_names[i] for i in indices], y=importances[indices])
plt.title('Importanza delle feature secondo Random Forest')
plt.xlabel('Feature')
plt.ylabel('Importanza')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# gridsearch
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Inizializza GridSearchCV per ottimizzare il modello
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

best1= grid_search.best_estimator_

# Predici sul test set con il modello ottimizzato
prev_ottimiz= best1.predict(X_test)

# classification report ottimizzato
report1 = classification_report(y_test, prev_ottimiz, target_names=wine.target_names)
print("Classification Report:\n", report1)

#matrice di confusione ottimizzata
matrice1 = confusion_matrix(y_test, prev_ottimiz)
sns.heatmap(matrice1, annot=True,
            xticklabels=wine.target_names,
            yticklabels=wine.target_names)

plt.title('Confusion Matrix ottimizzata')
plt.show()
