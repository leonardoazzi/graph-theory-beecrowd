# 1148 - PAÍSES DE GUERRA
# https://www.beecrowd.com.br/judge/pt/problems/view/1148

from collections import defaultdict
import sys

global graph
graph = defaultdict(list)

inf = sys.maxsize

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(v):
    if v not in graph:
        graph[v] = []

# Adiciona uma aresta ponderada entre dois vértices
# u: vértice de origem da aresta
# v: vértice de destino da aresta
# p: peso da aresta
def add_edge(u, v, p):
    graph[u].append([v, p]) 

def clear(v):
    for i in list(v.keys()):
        v[i]=False

def search(graph):
    visited = {}
    for i in graph.keys():
        visited[i]=False

# update_weight: Any, Any, int -> Dict
# Busca o vértice u como chave no dicionário e busca o vértice v como item 
# na lista de valores. Atualiza o w da lista.
def update_weight(u, v, new_weight):
    for idx, edge in enumerate(graph[u]):
        neighbour, _ = edge
        if neighbour == v:
            graph[u][idx][1] = new_weight

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

                    update_weight(i, n, 0)

# dijkstra: Any -> int
# Implementa o algoritmo de dijkstra para menor caminho em um grafo.
def dijkstra(u):
    distances = {v: inf-1 for v in graph}
    distances[u] = 0

    visited = set()
    
    while visited != set(distances):
        current_vertice = None
        shortest_distance = inf
        for v in graph:
            if v not in visited and distances[v] < shortest_distance:
                current_vertice = v
                shortest_distance = distances[v]

        visited.add(current_vertice)

        for neighbour, weight in graph[current_vertice]:
            if distances[current_vertice] + weight < distances[neighbour]:
                distances[neighbour] = distances[current_vertice] + weight

    return distances

# shortest_path_cost: Any, Any -> int
# Obtém o custo do menor caminho entre uma origem e um destino no grafo.
def shortest_path_cost(u, v):
    shortest_path = dijkstra(u)

    cost = inf
    for destiny, distance in shortest_path.items():
        if destiny == v:
            cost = distance
            if distance == (inf-1):
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

    N, E = first_line.split(" ")

    count = 0
    while (count < int(E)):
        acordo = input()
        X, Y, H = acordo.split(" ")
        add_edge(X, Y, int(H)) 
        count += 1

    verify_cycles(graph)

    K = int(input())

    count = 0
    results = []
    while (count < K):
        consulta = input()
        O, D = consulta.split(" ")

        print(shortest_path_cost(O, D))
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

    graph.clear()

    first_line = input()