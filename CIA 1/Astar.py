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

def a_star(start, goal):
    open_list = [(heuristic[start], 0, start)]
    heapq.heapify(open_list)
    closed_list = set()
    
    while open_list:
        _, g, current = heapq.heappop(open_list)
        
        if current == goal:
            return True
        
        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            f = g + cost + heuristic[neighbor]
            heapq.heappush(open_list, (f, g + cost, neighbor))

    return False

# Input: Start node 'S' and Goal node 'G'
print(a_star('S', 'G'))
