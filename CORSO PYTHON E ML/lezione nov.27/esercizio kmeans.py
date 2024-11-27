from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score,homogeneity_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset Iris
iris = load_iris()
X = iris.data
y = iris.target 

kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
kmeans.fit(X)
y_pred = kmeans.predict(X) 

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

centroids = kmeans.cluster_centers_
centroids_pca = pca.transform(centroids)


df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['cluster'] = y_pred  

plt.figure(figsize=(10,8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='cluster', palette='viridis', marker='o')
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], s=100, c='red', marker='X', label='Centroidi', edgecolor='red')
plt.title('Clustering K-Means sul dataset Iris con y pred_ (PCA 2D)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.legend(title='Cluster')
plt.show()


df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['cluster'] = y

plt.figure(figsize=(10,8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='cluster', palette='viridis', marker='o')
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], s=100, c='red', marker='X', label='Centroidi', edgecolor='red')
plt.title('Clustering K-Means sul dataset Iris (PCA 2D')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.legend(title='Cluster')
plt.show()

ars = adjusted_rand_score(y, y_pred)
hom = homogeneity_score(y, y_pred)

print(f"Adjusted  Rand Score:  {ars}")
print(f"Homogeneity Score: {hom}")

