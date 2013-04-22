import euler_tools as et


def get_solution_set():
    for center in get_centers():
        order_group = list()
        for i in range(5):
            b, c = int(center[i]), int(center[(i+1)%5])
            a = 14 - b - c
            order_group.append((a, b, c))
        print order_group


def get_centers():
    group = list()
    for p in et.permutations('12345'):
        sum_set = set()
        for i in range(5):
            sum_set.add(int(p[i]) + int(p[(i+1)%5]))
        if len(sum_set) != 5:
            continue
        in_order = sorted(sum_set)
        incremental = True
        for i in range(4):
            if in_order[i+1] - in_order[i] != 1:
                incremental = False
        if not incremental:
            continue
        if is_rotation(p, group):
            continue
        group.append(p)
    return group


def is_rotation(perm, group):
    for item in group:
        index = item.index(perm[0])
        mismatch = False
        for i in range(5):
            if perm[i] != item[(index + i) % 5]:
                mismatch = True
                break
        if not mismatch:
            return True
    return False
