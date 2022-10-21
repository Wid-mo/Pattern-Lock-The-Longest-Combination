P = {(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]}
print(P)
# points_avaidable_from_point = {
# p1: get_points_avaidable_from_point(p1) for p1 in P}


def distance(p1, p2):
    from math import hypot
    return hypot(p1[0] - p2[0], p1[1] - p2[1])


def is_point_between_two_points(p3, p1, p2):
    return distance(p3, p1) + distance(p3, p2) is distance(p1, p2)


def get_points_avaidable_from_point(p1):
    return {p2 for p2 in P if not is_point_between(p1, p2)}


def is_point_between(p1, p2):
    return any({is_point_between_two_points(p3, p1, p2)
                for p3 in P if p3 is not p1 if p3 is not p2
                })


points_avaidable_from_point = {
    p1: get_points_avaidable_from_point(p1) for p1 in P
}
points_avaidable_from_point[(-1, 1)]
# Example path
path = [(0, 0), (-1, 1)]
last_in_path = path[-1]
avaidable_points = set(filter(
    lambda point: point not in path,
    points_avaidable_from_point[last_in_path]))
print(avaidable_points)


def count_path_distance(path):
    return sum([distance(p1, p2) for p1, p2 in zip(path[:-1], path[1:])])


count_path_distance(path)

# Backtracking to find the longest length of path and
# all path with the longest length
the_longest_paths = []
max_length = 0
path = []


def DFS():
    global max_length
    if path:
        last_in_path = path[-1]
        avaidable_points = set(filter(
            lambda point: point not in path,
            points_avaidable_from_point[last_in_path]
        ))
    else:
        avaidable_points = P

    for choosing_point in avaidable_points:
        path.append(choosing_point)
        path_length = count_path_distance(path)
        if path_length > max_length:
            the_longest_paths.append(path)

        max_length = max(max_length, path_length)
        DFS()
        path.pop()


DFS()
print(max_length)

# filter all paths which haven't max_length
print(f'number of the longest paths before filter: {len(the_longest_paths)}')
the_longest_paths = list(filter(
    lambda path: count_path_distance(path) is max_length,
    the_longest_paths
))
print(f'number of the longest paths after filter: {len(the_longest_paths)}')
