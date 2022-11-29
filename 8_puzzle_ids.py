def id_dfs(puzzle, goal, get_moves):
    import itertools

    def dfs(route, depth):
        if depth == 0:
            return
        if route[-1] == goal:
            return route
        for move in get_moves(route[-1]):
            if move not in route:
                next_route = dfs(route + [move], depth - 1)
                if next_route:
                    return next_route

    for depth in itertools.count():
        route = dfs([puzzle], depth)
        if route:
            return route


puzzle, goal = [[1,2,5],[3,4,0],[6,7,8]], [[0,1,2],[3,4,5],[6,7,8]] # num_matrix(3, 3)
solution = id_dfs(puzzle, goal, num_moves(3, 3))
print(solution)

