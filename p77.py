import euler_tools

def solve(max_value=10**5, target=5000):
    primes = euler_tools.prime_sieve(max_value);
    current = 2
    while True:
    	ways = [0] * (current + 1)
    	ways[0] = 1
    	for i in range(0, len(primes)):
            for j in range(primes[i], current + 1):
                ways[j] += ways[j - primes[i]]
        if ways[current] >= target:
            return current
            #for i in range(len(ways)):
                #if ways[i] == target:
                    #return i
        current += 1
