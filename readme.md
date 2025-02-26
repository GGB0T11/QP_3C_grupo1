# **Conceitos fundamentais:**
	O clustering é uma técnica de aprendizado de máquina não supervisionado usada para 	identificar padrões ocultos em dados não rotulados. Ele agrupa elementos similares e separa os que possuem características distintas. A base matemática do clustering envolve métricas 	de distância, como a Euclidiana e a de Manhattan, para medir a similaridade entre pontos. Além disso, o objetivo central do clustering é minimizar a variabilidade dentro dos clusters e maximizar a diferença entre eles.

## **K-Means (Baseado em Partição):**
	O K-Means é um dos algoritmos de clustering mais usados e baseia-se na divisão dos dados em k grupos (partições). Cada grupo é representado pelo seu centróide, que é o ponto 	médio de todos os elementos do cluster.

	### **Como funciona?**
        1. Definir o número de clusters k.
        2. Selecionar k pontos aleatórios como centroides iniciais.
        3. Atribuir cada ponto ao centróide mais próximo (usando a distância Euclidiana).
        4. Atualizar os centroides calculando a média dos pontos em cada cluster.
        5. Repetir os passos 3 e 4 até que os centroides parem de mudar (convergência).

	### **Vantagens**
	    - Simples e eficiente para grandes conjuntos de dados.
		- Funciona bem em dados esféricos e bem separados.

	### **Desvantagens**
		- Precisa definir k previamente.
		- Sensível a valores atípicos e clusters de formas irregulares.

## **DBSCAN (Baseado em Densidade):**
	forma clusters com base na densidade dos pontos e pode detectar outliers automaticamente.

	### **Como funciona?**
        1. Define um raio de vizinhança (eps) e um número mínimo de pontos (min_samples).
        2. Identifica pontos centrais (pontos com pelo menos min_samples vizinhos dentro de eps).
        3. Expande clusters a partir desses pontos centrais, incluindo vizinhos próximos.
        4. Pontos que não pertencem a nenhum cluster são marcados como outliers (-1).

	### **Vantagens**
		- Detecta clusters de formas irregulares.
		- Identifica outliers automaticamente.

	### **Desvantagens**
		- Sensível à escolha de eps e min_samples.
		- Pode ter dificuldades em dados de alta dimensão.

## **Clustering Hierárquico:**
	cria uma estrutura de árvore (dendrograma) para organizar os dados. Ele pode ser de dois tipos:
        - **Aglomerativo (Bottom-Up):** Começa com cada ponto separado e vai unindo os mais próximos até formar um único cluster.
        -** Divisivo (Top-Down):** Começa com um único cluster e vai dividindo em subgrupos.

	### **Como funciona? (Método Aglomerativo)**
        1. Cada ponto começa como um cluster individual.
        2. Os clusters mais próximos são mesclados com base na distância.
        3. O processo continua até que reste apenas um cluster contendo todos os pontos.
        4. Podemos cortar o dendrograma para obter o número desejado de clusters.

	### **Vantagens**
 		- Não exige definir o número de clusters previamente.
		- Gera um dendrograma útil para análise exploratória.

	### **Desvantagens**
		- Computacionalmente mais pesado que K-Means para grandes conjuntos de dados.
		- Não lida bem com outliers.