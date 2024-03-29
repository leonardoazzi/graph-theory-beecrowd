# 1583 - CONTAMINAÇÃO
# https://www.beecrowd.com.br/judge/pt/problems/view/1583

from collections import defaultdict

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(graph, v):
	if v not in graph:
		graph[v] = []

# Adiciona uma aresta ponderada entre dois vértices
# u: vértice de origem da aresta
# v: vértice de destino da aresta
# p: peso da aresta
def add_bi_edge(graph, u, v):
	graph[u].append(v) 
	graph[v].append(u)

# update_weight: Any, Any, int -> Dict
# Busca o vértice u como chave no dicionário e busca o vértice v como item 
# na lista de valores. Atualiza o w da lista.
def update_weight(graph, u, v, new_weight):
	if v in graph[u][0][0]:
		graph[u][0][1] = new_weight

# connect_cells
# Compara vértices à esquerda e acima de um vértice de referência. Se os vértices
# adjacentes pertencem ao grafo de células (A ou T), eles são conectados com o 
# vértice de referência.
def connect_cells(graph, x, y, mapa): 
	
	# Esquerda
	vertex_ref = (x, y)
	vertex_left = (x-1, y)

	if vertex_ref in graph and vertex_left in graph:
		add_bi_edge(graph, vertex_ref, vertex_left)

	# Acima
	vertex_ref = (x, y)
	vertex_above = (x, y-1)

	if vertex_ref in graph and vertex_above in graph:
		add_bi_edge(graph, vertex_ref, vertex_above)

	return graph

# contaminar
# Utiliza DFS para buscar no mapa os vizinhos de vértices 'T' e substituir sua 
# célula para 'T' (contaminar)
def contaminar(grafo, vertice_inicio, map):
	fronteira = []
	visitados = set()

	fronteira.append(vertice_inicio)

	while fronteira:
		vertice = fronteira.pop()
		if vertice not in visitados:
			visitados.add(vertice)
			x, y = vertice
			map[x][y] = 'T'
			for vizinho in grafo[vertice]:
				fronteira.append(vizinho)

	return visitados

grafo = defaultdict(list)
first_input = input()

while(first_input != "0 0"):

	linhas, colunas = first_input.split(" ")

	N = int(linhas)
	M = int(colunas)

	if N > 50 or M > 50:
		continue
	
	T_coords = set()
	map = []
	row = 0
	while (row < N): # N linhas
		line_input = list(input())
		line_list = line_input[:M] # mantém na lista M caracteres

		map.append(line_list)
		for col, cell in enumerate(line_input, start=0):
			if cell == 'A' or cell == 'T':
				if cell == 'T': T_coords.add((row,col))
				add_vertex(grafo, (row,col))
				grafo = connect_cells(grafo, row, col, map)
		row += 1


	# Visitar todos os nodos do grafo a partir de uma coordenada T
	# Verificar se a próxima coordenada T já foi visitada
	# Se não, visitar próxima coordenada
	
	conjunto_visitas = set()
	for contaminant_xy in T_coords:

		if contaminant_xy not in conjunto_visitas:
			nodos_visitados = contaminar(grafo, contaminant_xy, map)
			conjunto_visitas = conjunto_visitas.union(nodos_visitados)

	# Saída
	linha = []
	for row in range(0, N):
		linha = map[row]
		result = ''.join(linha)
		print(result)
	
	print()

	grafo.clear()

	first_input = input()