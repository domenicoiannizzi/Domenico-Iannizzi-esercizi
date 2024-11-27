from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

diabete = load_diabetes()
X = diabete.data
y = diabete.target


df = pd.DataFrame(X, columns=diabete.feature_names)
df['target'] = y
df.astype(int)
print(df.describe())


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

modello = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None)
modello.fit(X_train, y_train)

previsioni = modello.predict(X_test)

mse = mean_squared_error(y_test, previsioni)
print("Mean Squared Error:", mse)

r2 = r2_score(y_test, previsioni)
print("R^2:", r2)

rmse = np.sqrt(mse)  
print("Root Mean Squared Error:", rmse)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, previsioni, color='blue', alpha=0.5)  
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)  
plt.title("Regressione Lineare")
plt.xlabel("y_test")
plt.ylabel("previsioni")
plt.grid()
plt.show()
