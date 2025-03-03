import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# Gerando dados sintéticos com 3 centros
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Plotando o dendrograma
linked = linkage(X, 'ward')
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.figure(figsize=(10, 7))
plt.title("Dendrograma")
plt.xlabel("Índice da Amostra")
plt.ylabel("Distância")
plt.show()

# Plotando os clusters
hc = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = hc.fit_predict(X)
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6, edgecolors='k')
plt.title("Clustering Hierárquico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid()
plt.show()