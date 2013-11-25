import euler_tools
import math

def solve(target = 50000000):
    primes = euler_tools.prime_sieve(int(math.sqrt(target)) + 1)
    squares = []
    cubes = []
    fourths = []
    for p in primes:
        squares.append(p**2)
    for p in primes:
        num = p**3
        if num > target:
            break
        cubes.append(num)
    for p in primes:
        num = p**4
        if num > target:
            break
        fourths.append(num)
    
    count = [0] * (target + 1)
    for s in squares:
        for c in cubes:
            for f in fourths:
                total = s + c + f
                if total <= target:
                    count[total] = 1
    return sum(count)
