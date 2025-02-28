import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. Gerar dados sintéticos
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=1.0, random_state=42)

# 2. Método do Cotovelo para determinar o melhor K
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
    print(f"K = {k}: Inércia = {kmeans.inertia_}")

# 3. Plotar o gráfico do Método do Cotovelo
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker='o', linestyle='--')
plt.title("Método do Cotovelo: Inércia vs Número de Clusters")
plt.xlabel("Número de Clusters (k)")
plt.ylabel("Inércia")
plt.xticks(k_values)
plt.grid()
plt.savefig("kmeans_inertia.png")  # Salvar o gráfico
plt.show()

# 4. Aplicar K-Means com o melhor K (neste caso, K=3)
best_k = 3  # Defina o melhor K com base no Método do Cotovelo
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
kmeans.fit(X)

# 5. Obter rótulos e centroides
labels = kmeans.labels_  # Rótulos dos clusters
centroids = kmeans.cluster_centers_  # Posições dos centroides

# 6. Plotar os clusters e centroides
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6, edgecolors='k')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title(f"K-Means com {best_k} Clusters")
plt.legend()
plt.savefig('kmeans_clusters.png')  # Salvar o gráfico
plt.show()