P = {(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]}
print(P)
# POINTS_AVAIDABLE_FROM_POINT = {
# p1: get_points_avaidable_from_point(p1) for p1 in P}


def distance(p1, p2):
    from math import hypot
    return hypot(p1[0] - p2[0], p1[1] - p2[1])


def is_point_between_two_points(p3, p1, p2):
    return distance(p3, p1) + distance(p3, p2) == distance(p1, p2)


def get_points_avaidable_from_point(p1):
    return {p2 for p2 in P if not is_point_between(p1, p2)}


def is_point_between(p1, p2):
    return any({is_point_between_two_points(p3, p1, p2)
                for p3 in P if p3 != p1 if p3 != p2
                })


POINTS_AVAIDABLE_FROM_POINT = {
    p1: get_points_avaidable_from_point(p1) for p1 in P
}
print(POINTS_AVAIDABLE_FROM_POINT[(-1, 1)])


# Example path
path = [(0, 0), (-1, 1)]
last_in_path = path[-1]
avaidable_points = POINTS_AVAIDABLE_FROM_POINT[last_in_path] - set(path)
print(avaidable_points)


def count_path_distance(path):
    return sum([distance(p1, p2) for p1, p2 in zip(path[:-1], path[1:])])


print(count_path_distance(path))


# Backtracking to find the longest length of path and
# all path with the longest length
the_longest_paths = []
max_length = 0
path = []


def DFS():
    global max_length
    if path:
        last_in_path = path[-1]
        avaidable_points = (POINTS_AVAIDABLE_FROM_POINT[last_in_path]
                            - set(path))
    else:
        avaidable_points = P.copy()

    for choosing_point in avaidable_points:
        path.append(choosing_point)
        path_length = count_path_distance(path)
        if path_length >= max_length:
            the_longest_paths.append(path.copy())

        max_length = max(max_length, path_length)
        DFS()
        path.pop()


DFS()
print(max_length)

# filter all paths which haven't max_length
the_longest_paths = [path for path in the_longest_paths
                     if count_path_distance(path) == max_length]
print(f'number of the longest paths: {len(the_longest_paths)}')

# There is 1-2 unique answers (we don't count rotations and flip).
# So, check some path
print(the_longest_paths[0])

# Yes, there is 1 solution.
# + 4 rotation
# + flip
# + two directional
