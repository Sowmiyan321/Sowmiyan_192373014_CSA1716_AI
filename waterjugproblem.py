from collections import deque

def water_jug(a, b, target):

    visited = set()
    queue = deque([(0, 0)])

    while queue:

        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        print((x, y))

        if x == target or y == target:
            print("Target Reached")
            return

        next_states = [
            (a, y),
            (x, b),
            (0, y),
            (x, 0),
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug(4, 3, 2)