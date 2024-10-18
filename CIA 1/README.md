# AI CIA-1
## SEARCH ALGORITHMS

This repository contains implementations of various search algorithms, including both heuristic-based and brute-force approaches. The algorithms are implemented in Python and designed to work on a predefined graph structure.

## Algorithms Included

1. **AO*** - A heuristic search algorithm that focuses on optimal paths using AND/OR trees.
2. **A*** - A widely-used heuristic search algorithm that combines the benefits of Dijkstra's and Greedy Best-First Search.
3. **Branch and Bound (Dead Horse)** - A systematic approach to explore all paths while maintaining the best path found.
4. **Branch and Bound (Hei)** - An enhanced version of the previous, considering heuristics for better performance.
5. **Breadth-First Search (BFS)** - An exhaustive search method that explores all neighbors before moving to the next level.
6. **Best Matching Search (BMS)** - A heuristic-based search that prioritizes nodes based on their estimated cost to the goal.
7. **Beam Search** - A variation of Best First Search that limits the number of nodes explored at each level (beam width).
8. **Best First Search** - A search algorithm that expands the node that appears to be closest to the goal.
9. **Branch and Bound** - A method for exploring all paths while maintaining the best solution found so far.
10. **Depth-First Search (DFS)** - A search algorithm that explores as far as possible along each branch before backtracking.
11. **Hill Climbing** - A local search algorithm that iteratively moves towards the direction of increasing value.
12. **British Museum Search** - A brute-force search algorithm that explores all possible paths to find a solution.

## Graph Structure

The algorithms use the following graph representation:

```python
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
    'S': 7,  # Estimated cost from S to goal
    'A': 6,  # Estimated cost from A to goal
    'B': 5,  # Estimated cost from B to goal
    'C': 8,  # Estimated cost from C to goal
    'D': 1,  # Estimated cost from D to goal
    'E': 9,  # Estimated cost from E to goal
    'G': 0   # Estimated cost from G to goal (goal node)
}
