from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Caricamento del dataset
digits = load_digits()
X = digits.data
y = digits.target

# Applicazione di PCA per ridurre a 2 componenti principali
pca = PCA(
    n_components=2,
    copy=True,
    whiten=False,
    svd_solver='auto',
    random_state=42
)
X_pca = pca.fit_transform(X)

# Visualizzazione dei dati ridotti
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='Spectral', edgecolor='k', s=40)
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.title('PCA sul Dataset Digits')
plt.colorbar(scatter)
plt.show()