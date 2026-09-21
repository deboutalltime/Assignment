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


def dfs():
    stack = [(start, [start])]
    visited = {start}
    expanded = 0

    while stack:
        current, path = stack.pop()
        expanded += 1

        if current == goal:
            return path, expanded

        r, c = current

        # reversed because Stack is LIFO
        for dr, dc in reversed(moves):
            nr, nc = r + dr, c + dc

            if (0 <= nr < 6 and
                0 <= nc < 6 and
                grid[nr][nc] != '#' and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None, expanded


path, expanded = dfs()

print("DFS path:")
print(path)

print("Path cost:", len(path) - 1)
print("Nodes expanded:", expanded)