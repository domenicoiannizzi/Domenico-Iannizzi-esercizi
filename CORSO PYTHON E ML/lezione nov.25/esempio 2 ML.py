#importazione dataset iris
from sklearn.datasets import load_iris
data = load_iris()
X = data.data  #caratteristiche
y = data.target  #target

#ridimensionamento dei dati
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#dati di test e train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#regressione lineare
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
#mse per la regressione lineare
from sklearn.metrics import mean_squared_error 
mse = mean_squared_error(y_test, predictions)



#KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X, y)
predictions = knn.predict(X)
#accuracy per il classificatore KNN
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)