import heapq

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

def best_first_search(start, goal):
    open_list = [(heuristic[start], start)]
    heapq.heapify(open_list)
    
    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return True

        for neighbor in graph[current]:
            heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return False

# Input: Start node 'S' and Goal node 'G'
print(best_first_search('S', 'G'))
