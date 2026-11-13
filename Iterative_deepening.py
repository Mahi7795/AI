
def depth_limited_search(graph, node, goal, limit, path):
    if node == goal:
        return path
    if limit == 0:
        return None

    for nxt in graph.get(node, []):
        if nxt not in path:
            result = depth_limited_search(
                graph, nxt, goal, limit - 1, path + [nxt]
            )
            if result is not None:
                return result
    return None

def iterative_deepening(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        print('Searching at depth:', limit)
        result = depth_limited_search(
            graph, start, goal, limit, [start]
        )
        if result is not None:
            return result
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

print('ITERATIVE DEEPENING SEARCH')
print('Nodes: A B C D E F G')

start = input('Enter start node: ').strip().upper()
goal = input('Enter goal node: ').strip().upper()

if start not in graph or goal not in graph:
    print('Invalid node.')
else:
    path = iterative_deepening(graph, start, goal, 4)
    print('Path found:', ' -> '.join(path) if path else 'Not found')
