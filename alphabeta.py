max_val, min_val = 1000, -1000

def fun_alphabeta(depth, node, max_player, values, alpha, beta):
    if depth == 3:
        return values[node]

    if max_player:
        best_val = min_val
        for i in range(2):
            value = fun_alphabeta(depth + 1, node * 2 + i, False, values, alpha, beta)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val
    else:
        best_val = max_val
        for i in range(2):
            value = fun_alphabeta(depth + 1, node * 2 + i, True, values, alpha, beta)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val

scores = [int(input("Enter node value: ")) for _ in range(int(input("Enter total number of leaf nodes: ")))]
depth = int(input("Enter depth value: "))
start_node = int(input("Enter node value: "))

print("The optimal value is:", fun_alphabeta(depth, start_node, True, scores, min_val, max_val))
