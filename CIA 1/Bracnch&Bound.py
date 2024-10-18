graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def branch_and_bound(start, goal):
    open_list = [(0, start, [])]
    min_cost = float('inf')
    best_path = []

    while open_list:
        cost, current, path = open_list.pop()

        if current == goal and cost < min_cost:
            min_cost = cost
            best_path = path + [current]

        for neighbor, edge_cost in graph[current].items():
            open_list.append((cost + edge_cost, neighbor, path + [current]))

    return best_path, min_cost

# Input: Start node 'S' and Goal node 'G'
print(branch_and_bound('S', 'G'))
