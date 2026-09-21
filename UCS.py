import heapq

grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)

# Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def ucs():
    # (cost, position, path)
    queue = [(0, start, [start])]
    visited = set()
    expanded = 0

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        if current == goal:
            return path, cost, expanded

        r, c = current

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (0 <= nr < 6 and
                0 <= nc < 6 and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                heapq.heappush(
                    queue,
                    (cost + 1, (nr, nc), path + [(nr, nc)])
                )

    return None, None, expanded


path, cost, expanded = ucs()

print("UCS path:")
print(path)

print("Path cost:", cost)
print("Nodes expanded:", expanded)