from collections import deque

def add_possible_solution(grid, q, path_map, g):
    if not grid.visited:
        q.append((grid.position.x, grid.position.y))
        path_map[grid.position] = g

def find_shortest_path(grid, start_node, end_node):
    if not grid:
        return []
    q = deque([(start_node.position.x, start_node.position.y)])
    m, n =  len(grid), len(grid[0])
    path_map = {}
    l = None

    # set all visited to false
    for i in range(m):
        for j in range(n):
            grid[i][j].visited = False

    while True:
        posx, posy = q.popleft()

        g = grid[posx][posy]

        if not g.passable or g.visited:
            continue

        if m > posx + 1:
            add_possible_solution(grid[posx + 1][posy], q, path_map, g)
        if posx > 0:
            add_possible_solution(grid[posx - 1][posy], q, path_map, g)
        if n > posy + 1:
            add_possible_solution(grid[posx][posy + 1], q, path_map, g)
        if posy > 0:
            add_possible_solution(grid[posx][posy - 1], q, path_map, g)
        
        g.visited = True

        if g.position == end_node.position:
            r = [g]
            while r[-1].position in path_map:
                r.append(path_map[r[-1].position])

            return list(reversed(r))

# https://www.codewars.com/kata/5573f28798d3a46a4900007a/train/python