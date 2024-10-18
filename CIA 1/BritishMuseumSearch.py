graph = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

def british_museum_search(start, goal):
    def explore_all_paths(current, path):
        if current == goal:
            return path

        if current not in graph or not graph[current]:
            return None

        for neighbor in graph[current]:
            result = explore_all_paths(neighbor, path + [neighbor])
            if result:  # If a valid path is found
                return result

        return None

    return explore_all_paths(start, [start])

# Input: Start node 'S' and Goal node 'G'
print(british_museum_search('S', 'G'))
