"""Esercizio: Classificazione di Cifre Scritte a Mano con Keras



In questo esercizio, costruiremo e addestreremo un semplice
modello di rete neurale utilizzando Keras per classificare le
cifre scritte a mano del dataset MNIST. 



Questo dataset contiene immagini in scala di grigi di cifre da 0
a 9, dimensionate a 28x28 pixel.



Obiettivi:

Caricare e preprocessare il dataset MNIST.
Costruire un modello sequenziale con strati densi.
Compilare il modello specificando ottimizzatore, funzione di
perdita e metriche.
Addestrare il modello sui dati di addestramento.
Valutare le prestazioni del modello sui dati di test.
Utilizzare il modello per fare predizioni su nuove immagini."""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix


# Caricamento del dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizzazione dei dati
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Reshape dei dati
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# Conversione delle etichette in formato one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Creazione del modello
model = Sequential()

# Aggiunta degli strati
model.add(Dense(128, input_dim=28*28, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax')) 


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1, verbose=2)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')

plt.plot(history.history['accuracy'],
label='Accuratezza Training')
plt.plot(history.history['val_accuracy'],
label='Accuratezza Validazione')
plt.xlabel('Epoca')
plt.ylabel('Accuratezza')
plt.legend()
plt.title('Andamento dell\'Accuratezza')
plt.show()


plt.plot(history.history['loss'],label='Perdita Training')
plt.plot(history.history['val_loss'], label='Perdita Validazione')
plt.xlabel('Epoca')
plt.ylabel('Perdita')
plt.legend()
plt.title('Andamento della Perdita')
plt.show()

predictions = model.predict(x_test)
# Conversione delle predizioni in etichette
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

conf_matrix = confusion_matrix(true_classes, predicted_classes)

plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()

# Visualizzazione di alcune predizioni
num_images = 5
random_indices = np.random.choice(len(X_test), num_images)
plt.figure(figsize=(15,3))
for i, idx in enumerate(random_indices):
    image = X_test[idx].reshape(28, 28)
    true_label = true_classes[idx]
    predicted_label = predicted_classes[idx]
    
    plt.subplot(1, num_images, i+1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')
plt.show()

# Random Forest Classifier 
y_train_rf = np.argmax(y_train, axis=1)  # Etichette in formato intero
y_test_rf = np.argmax(y_test, axis=1)

# Creazione e addestramento del modello Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train_rf)

# random forest predict e classification report
y_pred_rf = rf_model.predict(x_test)
cr = classification_report(y_test_rf, y_pred_rf)
print(f" classification report (Random Forest):{cr}")

# Cross-Validation su Random Forest 
cv_scores = cross_val_score(rf_model, x_train, y_train_rf, cv=5)
print(f"Cross-validated accuracy (Random Forest): {cv_scores.mean():.4f}")

# Predizioni con Random Forest 
predicted_rf_class = rf_model.predict(x_test[0].reshape(1, -1))
print(f"Predizione della Random Forest: {predicted_rf_class[0]}")
