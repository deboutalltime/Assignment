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

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def heuristic(position):
    r, c = position
    gr, gc = goal

    return abs(r - gr) + abs(c - gc)


def a_star():
    # (f, g, position, path)
    queue = [(heuristic(start), 0, start, [start])]

    visited = set()
    expanded = 0

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        if current == goal:
            return path, g, expanded

        r, c = current

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (0 <= nr < 6 and
                0 <= nc < 6 and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                new_g = g + 1
                new_f = new_g + heuristic((nr, nc))

                heapq.heappush(
                    queue,
                    (new_f, new_g, (nr, nc), path + [(nr, nc)])
                )

    return None, None, expanded


path, cost, expanded = a_star()

print("A* path:")
print(path)

print("Path cost:", cost)
print("Nodes expanded:", expanded)