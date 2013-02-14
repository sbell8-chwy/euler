

def f():
    power = 1
    num = 2
    count = 0
    while True:
        val = num**power
        lv = len(str(val))
        if lv == power:
            print '%d ** %d = %d, total: %d' % (num, power, val, count)
            count += 1
            num += 1
        if lv > power:
            if num == 2:
                break
            power += 1
            num = 2
        if lv < power:
            num += 1
    return count
