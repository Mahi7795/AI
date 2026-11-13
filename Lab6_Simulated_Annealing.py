
import math
import random

def fitness(x):
    return -(x - 5) ** 2 + 25

def simulated_annealing(start):
    random.seed(7)
    current = start
    best = current
    temperature = 10.0
    iteration = 0

    while temperature > 0.01:
        candidate = current + random.choice([-1, 1])
        difference = fitness(candidate) - fitness(current)

        if difference > 0 or random.random() < math.exp(
            difference / temperature
        ):
            current = candidate

        if fitness(current) > fitness(best):
            best = current

        iteration += 1
        temperature *= 0.9

    return best, iteration

print('SIMULATED ANNEALING ALGORITHM')
print('Maximize f(x) = -(x - 5)^2 + 25')

start = int(input('Enter starting x: '))

solution, count = simulated_annealing(start)

print('Iterations:', count)
print('Best solution x =', solution)
print('Best fitness =', fitness(solution))
