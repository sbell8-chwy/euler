import euler_tools as et

def cp():
    i = 12
    cd = {}
    smallest = {}
    while True:
        cubes = cubes_of_length(i)
        for c in cubes:
            split = split_string(c)
            if cd.has_key(split):
                cd[split] += 1
            else:
                cd[split] = 1
                smallest[split] = c
        for k, v in cd.iteritems():
            if v == 5:
                return smallest[k]
        i += 1


def split_string(string):
    chars = sorted(string)
    i = 0
    ret = []
    while i < len(chars):
        count = chars.count(chars[i])
        ret.append((chars[i], count))
        i += count
    return tuple(ret)


def cubes_of_length(length):
    i = 2
    cubes = list()
    max_val = int('9' * length)
    min_val = int('9' * (length - 1))
    while True:
        val = i**3
        if val > max_val:
            break
        if val > min_val:
            cubes.append(str(val))
        i += 1
    return cubes
