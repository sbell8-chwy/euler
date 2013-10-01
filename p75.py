import math
import fractions


def solve(max_perimeter=1000):
    int_triangles = [0] * (max_perimeter + 1)
    results = 0
    s2 = math.sqrt(2)
    for m in range(2, int(math.sqrt(max_perimeter/2))):
        for n in range(1, m):
            if (m - n) % 2 == 1 and fractions.gcd(m, n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2 * m * n
                p = a + b + c
                while p <= max_perimeter:
                    int_triangles[p] += 1
                    if int_triangles[p] == 1:
                        results += 1
                    if int_triangles[p] == 2:
                        results -= 1
                    p += a + b + c
    return results
