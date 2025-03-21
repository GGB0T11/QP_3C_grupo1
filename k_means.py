import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Gerando dados de exemplo com 3 centros
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=1.0, random_state=42)

# Inicializando o modelo KMeans com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
# Ajustando o modelo aos dados
kmeans.fit(X)

# Obtendo os rótulos dos clusters e os centróides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plotando os dados e os centróides
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=50, alpha=0.6, edgecolors="k")
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="X", s=200, label="Centroides")
plt.title(f"K-Means")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()