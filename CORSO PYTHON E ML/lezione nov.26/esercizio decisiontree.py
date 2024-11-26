from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Carico il dataset iris

iris = load_iris()
X = iris.data  
y = iris.target  

#standard scaler 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Suddivido il dataset in training set e test set

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Algoritmo Decision Tree
modello=DecisionTreeClassifier()

modello.fit(X_train, y_train)
previsioni=modello.predict(X_test)

report = classification_report(y_test, previsioni, target_names=iris.target_names)
print("Classification Report:\n", report)

cm = confusion_matrix(y_test, previsioni)

# Visualizzazione della matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)

plt.show()