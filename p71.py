def of():
    largest = 0
    sn = 1
    si = 1
    for i in range(2, 10**6):
        n = (i*3-1)/7
        val = float(n)/i
        if val > largest:
            largest = val
            sn = n
            si = i
    return sn, si

