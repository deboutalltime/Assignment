import heapq
from collections import deque

# 1. Create the grid
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
moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


# 2. BFS
def bfs():
    queue = deque()
    queue.append((start, [start]))

    visited = {start}
    expanded = 0

    while queue:
        current, path = queue.popleft()
        expanded += 1

        if current == goal:
            return path, len(path) - 1, expanded

        r, c = current

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < 6 and
                0 <= nc < 6 and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                queue.append(
                    ((nr, nc), path + [(nr, nc)])
                )

    return None, None, expanded


# 3. Manhattan heuristic
def heuristic(position):
    r, c = position
    return abs(r - goal[0]) + abs(c - goal[1])


# 4. A*
def a_star():
    # (f, g, position, path)
    queue = [
        (heuristic(start), 0, start, [start])
    ]

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
            nr = r + dr
            nc = c + dc

            if (0 <= nr < 6 and
                0 <= nc < 6 and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                new_g = g + 1
                new_f = new_g + heuristic((nr, nc))

                heapq.heappush(
                    queue,
                    (
                        new_f,
                        new_g,
                        (nr, nc),
                        path + [(nr, nc)]
                    )
                )

    return None, None, expanded


# 5. Run BFS
bfs_path, bfs_cost, bfs_expanded = bfs()

# 6. Run A*
astar_path, astar_cost, astar_expanded = a_star()


# 7. Print results
print("BFS")
print("Path:", bfs_path)
print("Cost:", bfs_cost)
print("Expanded:", bfs_expanded)

print("\nA*")
print("Path:", astar_path)
print("Cost:", astar_cost)
print("Expanded:", astar_expanded)

print("\nComparison")
print("--------------------------------")
print("Algorithm | Cost | Expanded")
print("--------------------------------")
print("BFS       |", bfs_cost, "  |", bfs_expanded)
print("A*        |", astar_cost, "  |", astar_expanded)