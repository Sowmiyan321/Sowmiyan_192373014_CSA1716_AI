from collections import deque

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    mr = 3 - m
    cr = 3 - c

    if mr > 0 and mr < cr:
        return False

    return True

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

queue = deque([((3,3,1), [])])
visited = set()

while queue:

    state, path = queue.popleft()

    if state in visited:
        continue

    visited.add(state)

    m, c, boat = state

    if state == (0,0,0):
        for step in path + [state]:
            print(step)
        break

    for dm, dc in moves:

        if boat == 1:
            new = (m-dm, c-dc, 0)
        else:
            new = (m+dm, c+dc, 1)

        if valid(new[0], new[1]):
            queue.append((new, path + [state]))