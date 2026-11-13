
from itertools import product

def implies(a, b):
    return (not a) or b

def kb_entails_query():
    print('KNOWLEDGE BASE: (P -> Q) AND P')
    print('QUERY: Q')
    print('P     Q     P->Q  KB    Query')
    print('--------------------------------')

    entails = True

    for p, q in product([False, True], repeat=2):
        implication = implies(p, q)
        kb = implication and p
        query = q

        print(
            f'{str(p):<6}'
            f'{str(q):<6}'
            f'{str(implication):<6}'
            f'{str(kb):<6}'
            f'{query}'
        )

        if kb and not query:
            entails = False

    return entails

print('PROPOSITIONAL LOGIC: TRUTH TABLE')

choice = input('Enter 1 to check KB entails Q: ').strip()

if choice == '1':
    if kb_entails_query():
        print('Entailment result: YES (KB entails Q)')
    else:
        print('Entailment result: NO')
else:
    print('Invalid option.')
