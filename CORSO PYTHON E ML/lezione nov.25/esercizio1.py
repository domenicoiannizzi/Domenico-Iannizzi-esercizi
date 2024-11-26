
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carico il dataset iris
iris = load_iris()
X = iris.data 
y = iris.target

#suddivido il dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#algoritmo KNN
algoritmo= KNeighborsClassifier(n_neighbors=5)
algoritmo.fit(X_train, y_train)
previsioni=algoritmo.predict(X_test)

#valuto l'accuratezza
accuracy = accuracy_score(y_test, previsioni)
print("Accuracy del modello KNN: ",accuracy)
