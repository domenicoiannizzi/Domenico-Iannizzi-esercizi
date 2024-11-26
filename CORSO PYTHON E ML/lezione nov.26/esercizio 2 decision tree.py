from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#carico il dataset wine
wine=load_wine()
#print(wine.DESCR)

X=wine.data
y=wine.target

#standard scaler 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#dati di test e train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#modello decision tree
modello=DecisionTreeClassifier()
modello.fit(X_train, y_train)
previsioni=modello.predict(X_test)

#classification report e matrice di confusione
report = classification_report(y_test, previsioni, target_names=wine.target_names)
print("Classification Report:\n", report)

matrice = confusion_matrix(y_test, previsioni)
sns.heatmap(matrice, annot=True,
            xticklabels=wine.target_names,
            yticklabels=wine.target_names)

plt.title('Confusion Matrix')
plt.show()