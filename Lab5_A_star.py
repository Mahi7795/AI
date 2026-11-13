
import heapq

def a_star(graph, heuristic, start, goal):
    frontier = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if g != best_cost.get(node):
            continue

        print('Exploring:', node, '| g =', g, '| f =', f)

        if node == goal:
            return path, g

        for nxt, weight in graph[node]:
            cost = g + weight
            if cost < best_cost.get(nxt, float('inf')):
                best_cost[nxt] = cost
                heapq.heappush(
                    frontier,
                    (cost + heuristic[nxt],
                     cost, nxt, path + [nxt])
                )

    return None, None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 4, 'B': 4, 'C': 2,
    'D': 5, 'E': 2, 'G': 0
}

print('A* SEARCH ALGORITHM')
print('Nodes: A B C D E G')

start = input('Enter start node: ').strip().upper()
goal = input('Enter goal node: ').strip().upper()

if start not in graph or goal not in graph:
    print('Invalid node.')
else:
    path, cost = a_star(graph, heuristic, start, goal)

    if path:
        print('Optimal path:', ' -> '.join(path))
        print('Total path cost:', cost)
    else:
        print('No path found.')
