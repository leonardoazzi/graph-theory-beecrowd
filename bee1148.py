# 1148 - PAÍSES DE GUERRA
# https://www.beecrowd.com.br/judge/pt/problems/view/1148

from collections import defaultdict
import sys
import heapq

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(graph, v):
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
	for edge in graph[u]:
		if v in edge:
			edge[1] = new_weight

# dijkstra: Any -> int
# Implementa o algoritmo de dijkstra para menor caminho em um grafo.
def dijkstra(graph, dist_dict, start_vertex, destiny_vertex):
	#print("DIJKSTRA DE", start_vertex, "PARA", destiny_vertex, "\n-------------------\n")
	#print("Grafo: ", graph, "\n")

	if len(dist_dict) == 0:
		distances = {v: float('infinity') for v in graph}
		distances[start_vertex] = 0
	else:
		if start_vertex in dist_dict:
			distances = dist_dict[start_vertex]
		else:
			distances = {v: float('infinity') for v in graph}
			distances[start_vertex] = 0

	#print("memória inicial\t", dist_dict)

	pred = {}
	visited = set()
	pq = []
	
	for v in distances:
		heapq.heappush(pq, (distances[v], v))

	while len(pq) > 0:
		_, current_vertex = heapq.heappop(pq)
		#print("visitados:\t", visited)
		#print("vertice atual:\t", current_vertex)

		#print("distancia até o destino\t", distances[destiny_vertex])
		
		if destiny_vertex in distances and distances[destiny_vertex] == float('infinity'):

				if current_vertex not in visited:
					visited.add(current_vertex)
					if current_vertex == destiny_vertex: return pred, distances

					for neighbour, weight in graph[current_vertex]:
						if neighbour in visited: continue
						updated_distance = distances[current_vertex] + weight
						if neighbour in distances and updated_distance < distances[neighbour]:
								distances[neighbour] = updated_distance
								pred[current_vertex] = neighbour
								heapq.heappush(pq, (updated_distance, neighbour))

		else:
			#print("SKIP!")
			return pred, distances
			
	return pred, distances

# shortest_path_cost: Any, Any -> int
# Obtém o custo do menor caminho entre uma origem e um destino no grafo.
def shortest_path_cost(graph, dist_dict, u, v):
	saved_paths, distances = dijkstra(graph, memory, u, v)

	if u not in memory:
		memory[u] = distances

	#print("Distâncias salvas\t", memory)

	#print("shortest path:\t", saved_paths)
	#print("distancia:\t", distances[v])

	cost = float('infinity')
	for destiny, distance in distances.items():
		if destiny == v:
			cost = distance
			if distance == float('infinity'):
				cost = "Nao e possivel entregar a carta"
	
	return cost

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

	memory = {}

	while (count < K):
		consulta = input()
		O, D = consulta.split(" ")

		if int(D) > N:
			continue
		
		res = shortest_path_cost(graph_1, memory, O, D)

		# print("\n---\nresultado\t",res, "\n---\n")
		print(res)

		count += 1

	print()

	graph_1.clear()
	memory.clear()
	dict_consultas.clear()

	first_line = input()