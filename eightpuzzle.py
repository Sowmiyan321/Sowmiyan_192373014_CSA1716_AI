from collections import deque

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

initial = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

def bfs(start, goal):

    queue = deque([(start, [])])
    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):

            if state_to_tuple(neighbor) not in visited:
                queue.append((neighbor, path + [current]))

    return None

solution = bfs(initial, goal)

if solution:
    print("Solution Found!\n")

    for step in solution:
        for row in step:
            print(row)
        print()

else:
    print("No Solution Exists.")