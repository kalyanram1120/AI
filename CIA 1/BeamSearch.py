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

def beam_search(start, goal, beam_width=2):
    open_list = [(heuristic[start], start)]
    
    while open_list:
        open_list.sort()
        open_list = open_list[:beam_width]
        
        next_list = []
        
        for _, current in open_list:
            if current == goal:
                return True
            
            for neighbor in graph[current]:
                next_list.append((heuristic[neighbor], neighbor))
        
        open_list = next_list

    return False

# Input: Start node 'S' and Goal node 'G'
print(beam_search('S', 'G'))
