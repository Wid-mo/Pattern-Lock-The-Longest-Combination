P = {(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]}
print(P)

# Print points avaidable from last point in path

path = [(-1, 1), (0, 0), (-1, 0)]


def points_avaidable_from_last_in_path(path):
    if not path:
        return P.copy()

    last_in_path = path[-1]
    return get_points_avaidable_from_point(last_in_path)


def get_points_avaidable_from_point(p1):
    points_not_in_path = P - set(path)
    return {p2 for p2 in points_not_in_path if not is_point_between(p1, p2)}


def is_point_between(p1, p2):
    points_not_in_path = P - set(path)
    return any({is_point_between_two_points(p3, p1, p2)
                for p3 in points_not_in_path if p3 != p1 if p3 != p2})


def is_point_between_two_points(p3, p1, p2):
    return distance(p3, p1) + distance(p3, p2) == distance(p1, p2)


def distance(p1, p2):
    from math import hypot
    return hypot(p1[0] - p2[0], p1[1] - p2[1])


print(points_avaidable_from_last_in_path(path))


# Path length

path = [(-1, 1), (0, 0)]


def count_path_length(path):
    return sum([distance(p1, p2) for p1, p2 in zip(path[:-1], path[1:])])


print(count_path_length(path))


# Backtracking to find max length
#     and all paths with the longest length

the_longest_paths = []
max_length = 0
path = []


def DFS():
    global max_length
    avaidable_points = points_avaidable_from_last_in_path(path)
    for choosed_point in avaidable_points:
        path.append(choosed_point)
        path_length = count_path_length(path)
        if path_length >= max_length:
            the_longest_paths.append(path.copy())

        max_length = max(max_length, path_length)
        DFS()
        path.pop()


DFS()
print(f'Length of the longest path: {max_length}')

# filter all paths which haven't max_length
the_longest_paths = [path for path in the_longest_paths
                     if count_path_length(path) == max_length]
print(f'Number of the longest paths: {len(the_longest_paths)}')

# without rotation and flipping there is ONE SOLUTION
print(the_longest_paths[0])

# Yes, there is 1 solution with:
#   4 rotation
#   flip
