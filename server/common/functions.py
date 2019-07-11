def flatten_2d(target_list):
    return list(_flatten_2d(target_list))


def _flatten_2d(target_list):
    for y in range(len(target_list)):
        for x in range(len(target_list[0])):
            yield target_list[y][x]


def gen_2d_list(axis_1, axis_2):
    ret_list = []
    for y in range(axis_1):
        ret_list.append([])
        for x in range(axis_2):
            ret_list[y].append(0)
    return ret_list


def dotest(name, func):
    print("\t" + str(name) + " ... ", end="")
    try:
        func()
        print("pass")
    except AssertionError as e:
        print("failed")
