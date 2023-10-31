struct = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
start_point = (0, 0)
exit_point = (0, len(struct[0]) - 1)
for i in range(len(struct)):
    if struct[i][0] == 0:
        start_point = (i, 0)
    if struct[i][-1] == 0:
        exit_point = (i, len(struct[0]) - 1)

def depth_first_search(current_point, exit_point, path=()):
    path += (current_point, )
    if exit_point == current_point:
        return path

    for y, x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        point = current_point[0] + y, current_point[1] + x
        if not (0 <= point[0] < len(struct) and 0 <= point[1] < len(struct[0])):
            continue
        if struct[point[0]][point[1]] == 1:
            continue

        if point in path:
            continue

        result = depth_first_search(point, exit_point, path)
        if result:
            return result

print(depth_first_search(start_point, exit_point))
