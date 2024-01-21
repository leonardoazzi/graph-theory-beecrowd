# 1148 - PAÍSES DE GUERRA
# https://www.beecrowd.com.br/judge/pt/problems/view/1148

from collections import defaultdict
import sys
import heapq

global graph
graph_1 = defaultdict(list)

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(graph, v):
	if v not in graph:
		graph[v] = []

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
	if v in graph[u][0][0]:
		graph[u][0][1] = new_weight


# verify_cycles: Dict -> Dict
# Verifica se existe um ciclo dentro do grafo e atualiza o peso
# das arestas
def verify_cycles(graph):
	# para cada vértice
	# for i in graph.keys():
	for i in list(graph):
		
		# para cada vizinho do vértice atual e peso da aresta
		for n, w in graph[i]:

			# para cada sucessor do vizinho e respectivo peso
			for nn, ww in graph[n]:
				
				# se o sucessor do vizinho for o próprio vértice atual
				if nn == i:

					update_weight(graph_1, i, n, 0)

# dijkstra: Any -> int
# Implementa o algoritmo de dijkstra para menor caminho em um grafo.
def dijkstra(graph, start_vertex):
	distances = {v: float('infinity') for v in graph}
	pred = {v: None for v in graph}

	distances[start_vertex] = 0
	pq = []
	visited = set()

	for v in distances:
		heapq.heappush(pq, (distances[v], v))

	while len(pq) > 0:
		_, current_vertex = heapq.heappop(pq)
		if current_vertex not in visited:
			visited.add(current_vertex)
			# if current_vertex == destiny: return cost

			for neighbour, weight in graph[current_vertex]:
				if neighbour in visited: continue
				updated_distance = distances[current_vertex] + weight
				if neighbour in distances:
					if updated_distance < distances[neighbour]:
						distances[neighbour] = updated_distance
						pred[neighbour] = current_vertex
						heapq.heappush(pq, (updated_distance, neighbour))
	return distances

# shortest_path_cost: Any, Any -> int
# Obtém o custo do menor caminho entre uma origem e um destino no grafo.
def shortest_path_cost(graph, u, v):
	shortest_path = dijkstra(graph, u)

	cost = float('infinity')
	for destiny, distance in shortest_path.items():
		if destiny == v:
			cost = distance
			if distance == float('infinity'):
				cost = "Nao e possivel entregar a carta"
	
	return cost

# ========== TESTES ==========
# print("\ngrafo 1")
# add_vertex('1')
# add_vertex('2')
# add_vertex('3')
# add_vertex('4')
# add_edge('1', '2', 5) 
# add_edge('2', '1', 10) 
# add_edge('3', '4', 8)
# add_edge('4', '3', 7)
# add_edge('2', '3', 6)
# verify_cycles(graph)


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
		add_edge(graph_1, X, Y, int(H)) 
		count += 1

	verify_cycles(graph_1)

	K = int(input())

	count = 0
	results = []
	while (count < K):
		consulta = input()
		O, D = consulta.split(" ")

		resultado = shortest_path_cost(graph_1, O, D)
		print(resultado)
		
		# results.append(shortest_path_cost(O, D))

		count += 1

	# for node in graph:
	#     origin = node
	#     shortest_path = dijkstra(origin)

	#     for destiny, distance in shortest_path.items():
	#         if distance == (inf-1):
	#             distance = "Nao e possivel entregar a carta"
	#         print(f"Caminho mais curto de {origin} para {destiny}: {distance}")

	# print(results)
	print("\n")

	graph_1.clear()

	first_line = input()