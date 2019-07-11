def flatten_2d(target_list):
    return list(_flatten_2d(target_list))


def _flatten_2d(target_list):
    for y in range(len(target_list)):
        for x in range(len(target_list[0])):
            yield target_list[y][x]