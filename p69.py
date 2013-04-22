import euler_tools as et


def tm():
    primes = et.prime_sieve()
    i = 0
    result = 1
    while result * primes[i] < 1000000:
        result *= primes[i]
        i += 1
    return result
