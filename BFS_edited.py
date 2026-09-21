from collections import deque

grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)

moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

queue = deque([(start, [start])])
visited = {start}

while queue:
    current, path = queue.popleft()

    if current == goal:
        print("BFS path:", path)
        print("Cost:", len(path) - 1)
        break

    r, c = current

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 6 and
            0 <= nc < 6 and
            grid[nr][nc] != '#' and
            (nr, nc) not in visited):

            visited.add((nr, nc))
            queue.append(
                ((nr, nc), path + [(nr, nc)])
            )