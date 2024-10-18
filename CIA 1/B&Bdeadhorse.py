graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def branch_bound_dead_horse(start, goal):
    path = []
    min_cost = float('inf')

    def recur_bb(node, cost):
        nonlocal min_cost
        if node == goal:
            min_cost = min(min_cost, cost)
            return True
        
        if node not in graph or not graph[node]:
            return False

        for neighbor, edge_cost in graph[node].items():
            if recur_bb(neighbor, cost + edge_cost):
                path.append(neighbor)

    recur_bb(start, 0)
    return path[::-1], min_cost

# Input: Start node 'S' and Goal node 'G'
print(branch_bound_dead_horse('S', 'G'))
