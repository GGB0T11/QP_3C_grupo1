# Conceitos Fundamentais

O **clustering** é uma técnica de aprendizado de máquina **não supervisionado** que agrupa elementos similares e separa os distintos, ajudando a identificar padrões ocultos em dados não rotulados.

### Base Matemática:
- Utiliza **métricas de distância** como **Euclidiana** e **Manhattan** para medir similaridade entre pontos.
- Objetivo:
  - **Minimizar** a variabilidade dentro dos clusters.
  - **Maximizar** a diferença entre eles.

---

# Algoritmos de Clustering

## K-Means (Baseado em Partição)

O **K-Means** divide os dados em **k grupos**, onde cada grupo é representado pelo seu **centróide** (média dos pontos do cluster).

### Como Funciona?
1. Definir **k clusters**.
2. Escolher **k centroides aleatórios**.
3. Atribuir cada ponto ao **centróide mais próximo**.
4. Atualizar os centroides recalculando a **média dos pontos** em cada cluster.
5. Repetir até que os centroides parem de mudar (**convergência**).

### Vantagens
- Simples e eficiente para **grandes conjuntos de dados**.
- Funciona bem para **dados bem separados**.

### Desvantagens
- Precisa definir **k previamente**.
- Sensível a **outliers** e formatos irregulares.

---

## DBSCAN (Baseado em Densidade)

O **DBSCAN** forma clusters baseando-se na **densidade dos pontos**, identificando automaticamente **outliers**.

### Como Funciona?
1. Define um **raio de vizinhança (eps)** e um **número mínimo de pontos (min_samples)**.
2. Identifica **pontos centrais** com **min_samples vizinhos dentro de eps**.
3. Expande clusters a partir desses **pontos centrais**.
4. Pontos isolados são marcados como **outliers (-1)**.

### Vantagens
- Detecta clusters de **formas irregulares**.
- Identifica **outliers automaticamente**.

### Desvantagens
- Sensível à escolha de **eps e min_samples**.
- Dificuldades com **dados de alta dimensão**.

---

## Clustering Hierárquico

Cria uma **estrutura de árvore (dendrograma)** para organizar os dados.

### Como Funciona? (Aglomerativo)
1. Cada ponto inicia como um **cluster individual**.
2. Os **clusters mais próximos** são mesclados.
3. O processo continua até restar **um único cluster**.
4. É possível **cortar o dendrograma** para definir o número desejado de clusters.

### Como Funciona? (Divisivo)
1. Começa com **todos os pontos em um único cluster**.
2. O cluster é dividido em **dois subgrupos**, considerando a maior dissimilaridade.
3. O processo continua **recursivamente** até atingir um número desejado de clusters.

### Vantagens
- Não exige definir **número de clusters previamente**.
- O **dendrograma** é útil para análise exploratória.

### Desvantagens
- Computacionalmente **pesado** para grandes conjuntos de dados.
- Sensível a **outliers**.

---

# Aplicação Prática

## Amazon (Segmentação de Clientes – K-Means)
A **Amazon** usa **K-Means** para segmentar clientes com base em:
- **Histórico de compras**
- **Comportamento de navegação**
- **Preferências**
Isso permite **recomendações personalizadas** e **ofertas direcionadas**.

## Spotify (Recomendação de Músicas – K-Means / Hierárquico)
O **Spotify** usa **clustering hierárquico** e **K-Means** para:
- Agrupar **usuários com gostos musicais semelhantes**.
- Organizar músicas com base em ritmo, gênero e frequência sonora.
- Criar playlists automáticas como **Discover Weekly**.

## Netflix (Recomendação de Filmes – K-Means / DBSCAN)
A **Netflix** usa **clustering** para:
- Identificar padrões de consumo.
- Sugerir séries e filmes **com base em gostos semelhantes**.
- Agrupar vídeos em categorias ocultas como subgêneros, tipo de narrativa e atores.