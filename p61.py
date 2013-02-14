import euler_tools as et

def cfn():
    """Cyclical figurate numbers"""
    tris = get_four_digit_nums(et.get_tri)
    sqrs = get_four_digit_nums(et.get_sqr)
    pents = get_four_digit_nums(et.get_pent)
    hexs = get_four_digit_nums(et.get_hex)
    hepts = get_four_digit_nums(et.get_hept)
    octs = get_four_digit_nums(et.get_oct)
    for t in tris:
        cycle = get_cycle([t], [sqrs, pents, hexs, hepts, octs])
        if cycle:
            total = sum([int(x) for x in cycle])
            return cycle, total


def get_cycle(current, nums2d):
    if len(nums2d) == 0:
        if current[0][:2] == current[-1][2:]:
            return current
        else:
            return None
    for i in range(len(nums2d)):
        # print '%d of %d' % (i, len(nums2d))
        num_list = nums2d[i]
        for j in range(len(num_list)):
            num = num_list[j]
            if current[-1][2:] == num[:2] and num not in current:
                new_cycle = current + [num]
                new_nums2d = nums2d[:i] + nums2d[i+1:]
                cycle = get_cycle(new_cycle, new_nums2d)
                if cycle:
                    return cycle
    return None


def get_four_digit_nums(f):
    nums = list()
    x = 1
    while True:
        n = f(x)
        if n > 9999:
            break;
        if n > 999:
            nums.append(str(n))
        x += 1
    return nums
