
print('VACUUM CLEANER AGENT')
print('Enter status as Dirty or Clean.')

rooms = {
    'A': input('Status of room A: ').strip().lower(),
    'B': input('Status of room B: ').strip().lower()
}

location = input('Initial location (A/B): ').strip().upper()

if location not in rooms or any(
    s not in ('dirty', 'clean') for s in rooms.values()
):
    print('Invalid room status or location.')
else:
    actions = 0
    for room in [location, 'B' if location == 'A' else 'A']:
        print('Agent at room', room)
        if rooms[room] == 'dirty':
            print('Action: SUCK (clean room ' + room + ')')
            rooms[room] = 'clean'
        else:
            print('Action: NO-OP (already clean)')

        actions += 1
        if actions == 1:
            print('Action: MOVE to other room')

    print('Final state: A =', rooms['A'], ', B =', rooms['B'])
    print('All rooms are clean!')
