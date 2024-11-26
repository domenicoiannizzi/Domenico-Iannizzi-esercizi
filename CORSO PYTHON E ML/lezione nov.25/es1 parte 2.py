from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

# Carico il dataset iris
iris = load_iris()
X = iris.data 
y = iris.target 

#suddivido il dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#modello regressione lineare
modello = LinearRegression()

modello.fit(X, y)

previsioni = np.round(modello.predict(X_test)).astype(int)

#accuracy score
accuracy = accuracy_score(y_test, previsioni)
print(f"Accuratezza del modello: {accuracy:.2f}")

