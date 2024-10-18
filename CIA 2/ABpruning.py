def alpha_beta_pruning(depth, nodeIndex, isMax, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if isMax:
        maxEval = float('-inf')
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

if __name__ == "__main__":
    n = int(input("Enter the number of values (should be 8 for a complete binary tree of depth 3): "))
    
    if n != 8:
        print("The number of values must be 8.")
    else:
        print("Enter the values (space-separated): ")
        values = list(map(int, input().split()))

        if len(values) != n:
            print("You must enter exactly 8 values.")
        else:
            alpha = float('-inf')
            beta = float('inf')
            optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta)
            print(f"Optimal value using Alpha-Beta Pruning: {optimal_value}")
