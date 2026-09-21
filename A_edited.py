import heapq

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

def heuristic(position):
    r, c = position
    return abs(r - 5) + abs(c - 5)

queue = [(heuristic(start), 0, start, [start])]
visited = set()

while queue:
    f, g, current, path = heapq.heappop(queue)

    if current in visited:
        continue

    visited.add(current)

    if current == goal:
        print("A* path:", path)
        print("Cost:", g)
        break

    r, c = current

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 6 and
            0 <= nc < 6 and
            grid[nr][nc] != '#' and
            (nr, nc) not in visited):

            new_g = g + 1
            h = heuristic((nr, nc))
            f = new_g + h

            heapq.heappush(
                queue,
                (f, new_g, (nr, nc), path + [(nr, nc)])
            )