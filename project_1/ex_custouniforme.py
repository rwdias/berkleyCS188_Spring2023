import heapq

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parents = {}
    
    while queue:
        current_cost, current_node = heapq.heappop(queue)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = parents.get(current_node)
            return path
        
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node
                heapq.heappush(queue, (new_cost, neighbor))
    
    return None

# Exemplo de grafo com pesos (dicionário de dicionários)
graph = {
    'A': {'B': 14, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
goal_node = 'D'
shortest_path = dijkstra(graph, start_node, goal_node)
print("Caminho mais curto:", shortest_path)
