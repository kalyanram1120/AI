from collections import deque

graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def bfs(start, goal):
    queue = deque([start])
    visited = set()
    
    while queue:
        current = queue.popleft()

        if current == goal:
            return True
        
        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False

# Input: Start node 'S' and Goal node 'G'
print(bfs('S', 'G'))
