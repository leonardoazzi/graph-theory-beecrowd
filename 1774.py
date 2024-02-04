# 1774 - ROTEADORES
# https://www.beecrowd.com.br/judge/pt/problems/view/1774

from collections import defaultdict

class UnionFind:
	def __init__(self, numOfElements):
		self.parent = self.makeSet(numOfElements) # Cria um conjunto do tamanho do número de elementos
		self.size = [1] * numOfElements # Cria uma lista de 1 do tamanho do numOfElements
		self.count = numOfElements

	def makeSet(self, numOfElements):
		return [x for x in range(numOfElements)] # Cria um array de 0 ao numOfElements
	
	def findPathCompression(self, node):
		while node != self.parent[node]:
			self.parent[node] = self.parent[self.parent[node]] # Otimização Path compression
			node = self.parent[node]
		return node

	def find(self, i): # Sem path compression, implementação recursiva
		if self.parent[i] == i:
			return i
		else:
			return self.find(self.parent[i])
		
	def union(self, x, y):
		x_root = self.findPathCompression(x)
		y_root = self.findPathCompression(y)
		
		if x_root == y_root:
			return False
		
		if self.size[x_root] > self.size[y_root]:
			self.parent[y_root] = x_root
			self.size[x_root] += 1
		else:
			self.parent[x_root] = y_root
			self.size[y_root] += 1

		self.count -= 1 # Diminui a contagem do número de elementos ao agregá-los
		return True

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(graph, v):
	if v not in graph:
		graph[v].append('')

# Adiciona uma aresta ponderada entre dois vértices
# u: vértice de origem da aresta
# v: vértice de destino da aresta
# p: peso da aresta
def add_bi_edge(graph, u, v, p):
	graph[u].append([v, p]) 
	graph[v].append([u, p]) 

# update_weight: Any, Any, int -> Dict
# Busca o vértice u como chave no dicionário e busca o vértice v como item 
# na lista de valores. Atualiza o w da lista.
def update_weight(graph, u, v, new_weight):
	for edge in graph[u]:
		if v in edge:
			edge[1] = new_weight

def select_weight(e):
	return e[1]

def kruskal(edges_ascending, num_of_elements):
	A = []
	edge_count = 0

	uf = UnionFind(num_of_elements+1)

	min_weight = 0
	for edge, weight in edges_ascending:
		u, v = edge

		if uf.union(u,v):
			min_weight += weight
			edge_count += 1
			A.append((u, v))
			if edge_count == num_of_elements - 1:
				return min_weight
	
	return min_weight


if __name__ == "__main__":
	grafo = defaultdict(list)
	first_input = input()

	roteadores, cabos = first_input.split(" ")

	R = int(roteadores)
	C = int(cabos)

	# if R > 50 or C > 50:
	# 	exit()

	edges_list = []

	row = 0
	while (row < C): # N linhas
		entrada = input()
		V, W, P = entrada.split(" ")

		add_bi_edge(grafo, V, W, int(P))
		
		edges_list.append(([int(V), int(W)], int(P)))

		row += 1

	num_elements = len(grafo)

	edges_list.sort(key=select_weight)
	
	minimum_weight = kruskal(edges_list, num_elements)

	print(minimum_weight)