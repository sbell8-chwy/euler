import sys

TARGET = 2000000

def compute_sum(count):
    if count == 1 or count == 0:
        return count
    return (count**2 + count) / 2


def count_rects(n, m):
    return compute_sum(m) * compute_sum(n)


def compute_mid(imin, imax):
    if imax == -1:
        return imin * 2
    return (imin + imax) / 2


def best_rec_for_m(m, target):
    best_count = sys.maxint
    best_size = (1, 1)
    imin = m
    imax = -1
    while imax == -1 or imax >= imin:
        imid = compute_mid(imin, imax)
        count = count_rects(imid, m)
        if abs(target - count) < best_count:
            best_count = abs(target - count)
            best_size = (imin, m)
        if count > target:
            imax = imid - 1
        elif count < target:
            imin = imid + 1
        else:
            break
    return best_size, best_count

   
def solve():
    m = 1
    smallest_count = sys.maxint
    closest_value = 0
    closest_size = (1, 1)
    while True:
        size, count = best_rec_for_m(m, TARGET)
        if smallest_count > count:
            smallest_count = count
            closest_value = count_rects(size[0], size[1])
            closest_size = size
        if size[0] == size[1]:
            break
        m += 1
    return closest_size, closest_value
