import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Calculando a inércia para diferentes valores de k
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plotando o gráfico do método do cotovelo
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker="o", linestyle="--")
plt.title("Método do Cotovelo")
plt.xlabel("Número de Clusters (k)")
plt.ylabel("Inércia")
plt.xticks(k_values)
plt.grid()
plt.show()