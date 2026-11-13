
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new = list(state)
            other = nr * 3 + nc
            new[zero], new[other] = new[other], new[zero]
            yield tuple(new)

def solve(start):
    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            if nxt not in parent:
                parent[nxt] = state
                queue.append(nxt)
    return None

def show(state):
    for i in range(0, 9, 3):
        print(' '.join('_' if n == 0 else str(n)
                       for n in state[i:i+3]))

print('8-PUZZLE SOLVER (BFS)')
print('Enter 9 numbers (0 represents blank):')
start = tuple(map(int, input().split()))

if len(start) != 9 or set(start) != set(range(9)):
    print('Invalid puzzle: enter each number from 0 to 8 once.')
else:
    result = solve(start)
    if result is None:
        print('No solution exists.')
    else:
        print('Moves required:', len(result) - 1)
        for step, board in enumerate(result):
            print('Step', step)
            show(board)
            print()
