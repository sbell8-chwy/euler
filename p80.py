from decimal import *
import euler_tools as et

def solve():
    getcontext().prec = 101
    total = 0
    for i in range(2, 100):
        if et.is_sqr(i):
            continue
        total += sum(Decimal(i).sqrt().as_tuple().digits[:100])
    return total
        
