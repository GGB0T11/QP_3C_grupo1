import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Gerando dados sintéticos com 3 centros
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Padronizando os dados para ter média 0 e variância 1
X = StandardScaler().fit_transform(X)

# Aplicando o algoritmo DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X)

# Obtendo os rótulos dos clusters
labels = dbscan.labels_

# Plotando os clusters
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=50, alpha=0.6, edgecolors="k")
plt.title(f"DBSCAN")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid()
plt.show()