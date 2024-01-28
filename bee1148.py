# 1148 - PAÍSES DE GUERRA
# https://www.beecrowd.com.br/judge/pt/problems/view/1148

from collections import defaultdict
import sys
import heapq

# Cria uma matriz de adjacência preenchida por zeros
# V: número de vértices
def create_adjacency_matrix(V, p_value):
	matrix = []
	for _ in range(0, V+1):
		row = []
		for _ in range(0, V+1):
			row.append(p_value)
		matrix.append(row)

	return matrix

# Adiciona uma aresta ponderada entre dois vértices
# u: vértice de origem da aresta
# v: vértice de destino da aresta
# p: peso da aresta
def add_edge(graph, u, v, p):
	graph[u].append([v, p]) 

# update_weight: Any, Any, int -> Dict
# Busca o vértice u como chave no dicionário e busca o vértice v como item 
# na lista de valores. Atualiza o w da lista.
def update_weight(graph, u, v, new_weight):
	for edge in graph[u]:
		if v in edge:
			edge[1] = new_weight

# dijkstra: Any -> int
# Implementa o algoritmo de dijkstra para menor caminho em um grafo.
# def dijkstra(graph, dist_dict, start_vertex, destiny_vertex):

# 	if len(dist_dict) == 0:
# 		distances = {v: float('infinity') for v in graph}
# 		distances[start_vertex] = 0
# 	else:
# 		if start_vertex in dist_dict:
# 			distances = dist_dict[start_vertex]
# 		else:
# 			distances = {v: float('infinity') for v in graph}
# 			distances[start_vertex] = 0
# 	pred = {}
# 	visited = set()
# 	pq = []
	
# 	for v in distances:
# 		heapq.heappush(pq, (distances[v], v))

# 	while len(pq) > 0:
# 		_, current_vertex = heapq.heappop(pq)
		
# 		if destiny_vertex in distances and distances[destiny_vertex] == float('infinity'):

# 				if current_vertex not in visited:
# 					visited.add(current_vertex)
# 					if current_vertex == destiny_vertex: return pred, distances

# 					for neighbour, weight in graph[current_vertex]:
# 						if neighbour in visited: continue
# 						updated_distance = distances[current_vertex] + weight
# 						if neighbour in distances and updated_distance < distances[neighbour]:
# 								distances[neighbour] = updated_distance
# 								pred[current_vertex] = neighbour
# 								heapq.heappush(pq, (updated_distance, neighbour))

# 		else:
# 			return pred, distances
			
# 	return pred, distances

# dijkstra: Any -> int
# Implementa o algoritmo de dijkstra para menor caminho em um grafo.
def dijkstra2(graph, dist_matrix, start_vertex, destiny_vertex):

	if len(dist_matrix) == 0:
		distances = create_adjacency_matrix(len(graph), float('infinity'))
	else:
		distances = dist_matrix

	distances[start_vertex][start_vertex] = 0
	pred = {}
	visited = set()

	pq = []
	
	for vertex in range(1, len(distances)):
		heapq.heappush(pq, (distances[start_vertex][vertex], vertex))

	while len(pq) > 0:
		_, current_vertex = heapq.heappop(pq)
		
		if distances[start_vertex][destiny_vertex] == float('infinity'):

			if current_vertex not in visited:
				visited.add(current_vertex)

				# Se chegou ao vértice de destino, retornar
				if current_vertex == destiny_vertex: return pred, distances

				for neighbour, weight in graph[str(current_vertex)]:
					if neighbour in visited: continue
					updated_distance = distances[start_vertex][current_vertex] + weight

					if updated_distance < distances[start_vertex][int(neighbour)]:
							distances[start_vertex][int(neighbour)] = updated_distance
							pred[current_vertex] = neighbour
							heapq.heappush(pq, (updated_distance, int(neighbour)))
				if current_vertex == destiny_vertex: return pred, distances
		else:
			return pred, distances

# shortest_path_cost: Any, Any -> int
# Obtém o custo do menor caminho entre uma origem e um destino no grafo.
def shortest_path_cost(graph, distances, u, v):
	_, distances = dijkstra2(graph, distances, u, v)

	cost = distances[u][v]
	if cost == float('infinity'):
		cost = "Nao e possivel entregar a carta"
	
	return distances, cost

graph_1 = defaultdict(list)
dict_consultas = defaultdict(list)

first_line = input()

while(first_line != "0 0"):

	cidades, acordos = first_line.split(" ")

	N = int(cidades)
	E = int(acordos)

	if N > 500 or E > (N**2):
		continue

	count = 0
	while (count < int(E)):
		acordo = input()
		X, Y, H = acordo.split(" ")

		if int(Y) > N or int(H) > 1000:
			continue

		add_edge(graph_1, X, Y, int(H)) 

		for pair in graph_1[Y]:
			if pair[0] == X:
				update_weight(graph_1, Y, X, 0)
				update_weight(graph_1, X, Y, 0)

		count += 1

	K = int(input())

	count = 0
	results = []

	if K > 100:
			continue

	graph_save = []

	while (count < K):
		consulta = input()
		O, D = consulta.split(" ")

		O = int(O)
		D = int(D)

		if D > N:
			continue
		
		graph_save, res = shortest_path_cost(graph_1, graph_save, O, D)

		# print("---\nresultado\t",res, "\n---")
		print(res)

		count += 1

	print()

	graph_1.clear()
	dict_consultas.clear()

	first_line = input()