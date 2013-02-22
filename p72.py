

def cf(num):
    phi_list = phis(num + 1)
    count = 0
    for i in range(2, num + 1):
        count += phi_list[i]
    return count


def phis(num):
    retval = [1 for i in range(num)]
    for i in range(2, num):
        if retval[i] == 1:
            for j in range(i, num, i):
                retval[j] *= i - 1
                k = j / i
                while k % i == 0:
                    retval[j] *= i
                    k /= i
    return retval
