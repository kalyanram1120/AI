graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

def ao_star(start, goal):
    def recur_ao_star(curr_node):
        print(f"Visiting: {curr_node}")
        if curr_node == goal:
            return True
        
        if curr_node not in graph or not graph[curr_node]:
            return False
        
        min_cost = float('inf')
        best_path = None

        for neighbor, cost in graph[curr_node].items():
            temp_cost = cost + heuristic[neighbor]
            if temp_cost < min_cost:
                min_cost = temp_cost
                best_path = neighbor

        if best_path:
            return recur_ao_star(best_path)
        
        return False

    return recur_ao_star(start)

# Input: Start node 'S' and Goal node 'G'
print(ao_star('S', 'G'))
