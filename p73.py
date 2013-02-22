import fractions


def frac_in_range():
    count = 0
    limit = 12000
    for i in range(5, limit + 1):
        for j in range(((i-1)/3)+1, ((i-1)/2) + 1):
            if fractions.gcd(i, j) == 1:
                count += 1
    return count
