import fractions


def totient_perm():
    min_ratio = -1
    mini = 0
    i = 2
    phi_list = phis(10**7 + 1)
    while i <= 10**7:
        p = phi_list[i]
        if is_perm(i, p):
            ratio = float(i)/p
            if min_ratio == -1 or ratio < min_ratio:
                min_ratio = ratio
                mini = i
        i += 1
    return mini, min_ratio


def is_perm(one, two):
    o = list(str(one))
    t = list(str(two))
    if len(o) != len(t):
        return False
    o.sort()
    t.sort()
    for i in range(len(o)):
        if o[i] != t[i]:
            return False
    return True


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


def phi(num):
    if num == 1:
        return 1
    i = 1
    count = 0
    while i < num:
        gcd = fractions.gcd(i, num)
        if gcd == 1:
            count += 1
        i += 1
    return count
