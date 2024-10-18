graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def oracle_search(start, goal):
    # Assume we magically know the best path (for demonstration)
    best_path = ['S', 'A', 'D', 'G']
    return best_path if start == 'S' and goal == 'G' else None

# Input: Start node 'S' and Goal node 'G'
print(oracle_search('S', 'G'))
