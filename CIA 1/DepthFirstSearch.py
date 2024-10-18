graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def dfs(start, goal):
    stack = [start]
    visited = set()
    
    while stack:
        current = stack.pop()
        
        if current == goal:
            return True
        
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])
            
    return False

# Input: Start node 'S' and Goal node 'G'
print(dfs('S', 'G'))
