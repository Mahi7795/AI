
def fitness(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start

    while True:
        print('Current x =', current,
              '| fitness =', fitness(current))

        neighbors = [current - 1, current + 1]
        best = max(neighbors, key=fitness)

        if fitness(best) <= fitness(current):
            return current

        current = best

print('HILL CLIMBING ALGORITHM')
print('Maximize f(x) = -(x - 5)^2 + 25')

start = int(input('Enter starting x: '))

answer = hill_climbing(start)

print('Best solution x =', answer)
print('Maximum fitness =', fitness(answer))
