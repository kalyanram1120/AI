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

def hill_climbing(start, goal):
    current = start
    
    while current != goal:
        print(f"Visiting: {current}")
        neighbors = graph[current]
        if not neighbors:
            return False

        current = min(neighbors, key=lambda x: heuristic[x])

    return True

# Input: Start node 'S' and Goal node 'G'
print(hill_climbing('S', 'G'))
