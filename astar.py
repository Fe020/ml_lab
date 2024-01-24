import heapq

example_map = {'S': {'A': 1, 'G': 10}, 'A': {'B': 2, 'C': 1, 'S': 1}, 'B': {'D': 5, 'A': 2},
               'C': {'D': 3, 'G': 4, 'A': 1}, 'D': {'G': 2, 'C': 3, 'B': 5}, 'G': {'S': 10, 'C': 4, 'D': 2}}

heuristic1 = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0}

def a_star_search(graph, start, goal, heuristic):
    open_list, closed_set, g = [(0, start)], set(), {loc: float('inf') for loc in graph}
    g[start] = 0
    while open_list:
        current_g, current_node = heapq.heappop(open_list)
        if current_node == goal: return g[goal]
        if current_node in closed_set: continue
        closed_set.add(current_node)
        for neighbor, dist in graph[current_node].items():
            tent_g = g[current_node] + dist
            if tent_g < g[neighbor]:
                g[neighbor] = tent_g
                heapq.heappush(open_list, (tent_g + heuristic[neighbor], neighbor))
    return float('inf')

start, goal = 'S', 'G'
shortest_distance = a_star_search(example_map, start, goal, heuristic1)
print(f"The shortest distance from {start} to {goal} is {shortest_distance} km." if shortest_distance < float('inf') else f"No path found from {start} to {goal}.")
