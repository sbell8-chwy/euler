import math


def permutations(string):
    if not string:
        yield ''
    for i, d in enumerate(string):
        perms = permutations(string[:i] + string[i+1:])
        for perm in perms:
            yield d + perm


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def prime_sieve(max_value=10**6):
    if max_value == 2:
        return [2]
    if max_value < 2:
        return []
    s = range(3, max_value + 1, 2)
    mroot = max_value ** 0.5
    half = (max_value + 1) / 2 - 1
    i = 0
    m = 3
    while m < mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]

def is_palindrome(item):
    s = str(item)
    half = len(s) / 2
    for i in range(half):
        if s[i] != s[(i + 1) * -1]:
            return False
    return True

def is_sqr(x):
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root*root == x


get_tri = lambda(x): x*(x+1)/2
get_sqr = lambda(x): x**2
get_pent = lambda(x): x*(3*x-1)/2
get_hex = lambda(x): x*(2*x-1)
get_hept = lambda(x): x*(5*x-3)/2
get_oct = lambda(x): x*(3*x-2)

is_tri = lambda(x): is_sqr(8*x+1)
is_pent = lambda(x): is_sqr(24*x+1)
is_hex = lambda(x): is_tri(x) and (1+math.sqrt(8*x+1)) % 4 == 0
