
def solve(max_number=100):
    counts = [0,0]
    for n in range(2, max_number + 1):
        count = n - 1
        mid = n/2
        count += sum(counts[:mid + 1])
        if n % 2 == 0:
            mid -= 1
        count += sum(counts[:mid + 1])
        counts.append(count)
    return counts


def other_solve(target = 100):
    ways = [0] * (target + 1);
    ways[0] = 1;
 
    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    return ways
