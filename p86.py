import euler_tools
import math


def compute_square_distance(a, b, c):
    return (a + b)**2 + c**2


def is_integer_solution(a, b, c):
    csd = compute_square_distance
    min_square_distance = min(csd(a,b,c), csd(b,c,a), csd(c,a,b))
    return euler_tools.is_sqr(min_square_distance)


def compute_integer_solutions(m):
    solution_count = 0
    i = 1
    while i <= m:
        j = i
	while j <= m:
	    k = j
	    while k <= m:
	        if is_integer_solution(i, j, k):
		    solution_count += 1
		k += 1
	    j += 1
	i += 1
    return solution_count


def compute_mid(imin, imax):
    if imax == -1:
        return imin * 2
    return (imin + imax) / 2


#Takes too long
def solve(target = 10**6):
    imin = 1000
    imax = -1
    closest_over = -1
    while imax == -1 or imax >= imin:
        imid = compute_mid(imin, imax)
	count = compute_integer_solutions(imid)
	if count < target:
	    imin = imid + 1
	if count > target:
	    imax = imid - 1
	    closest_over = imid
    return closest_over


def solve_2(target = 10**6):
    length = 2
    count = 0
    while count < target:
        length += 1
	wh = 3
	while wh <= 2 * length:
	    square_distance = wh**2 + length**2
	    if euler_tools.is_sqr(square_distance):
	        if wh <= length:
		    count += wh / 2
		else:
		    count += 1 + (length - (wh + 1) / 2)
            wh += 1
    return length
