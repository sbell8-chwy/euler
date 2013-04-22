import euler_tools as et
import operator
import math


def prime_pair_sets():
    primes = et.prime_sieve(10**4)
    prime_count = len(primes)
    min_sum = -1
    for a in range(prime_count):
        print a
        for b in range(a+1, prime_count):
            if not test_primes((primes[a], primes[b])):
                continue
            for c in range(b+1, prime_count):
                if not test_primes((primes[a], primes[b], primes[c])):
                    continue
                for d in range(c+1, prime_count):
                    if not test_primes((primes[a], primes[b], primes[c], primes[d])):
                        continue
                    for e in range(d+1, prime_count):
                        prime_set = primes[a], primes[b], primes[c], primes[d], primes[e]
                        if test_primes(prime_set):
                            if min_sum == -1 or min_sum > sum(prime_set):
                                min_sum = sum(prime_set)
                                print min_sum
    return min_sum


def test_primes(primes):
    lp = len(primes)
    for i in range(lp):
        for j in range(i+1, lp):
            si = str(primes[i])
            sj = str(primes[j])
            if not et.is_prime(int(si + sj)):
                return False
            if not et.is_prime(int(sj + si)):
                return False
    return True

def xor_decode():
    chars = open('cipher1.txt').readline().rstrip().split(',')
    nums = [int(x) for x in chars]
    ds = 'god'
    attempt = decrypt(nums, ds)
    if attempt and 32 in attempt:
        print ds
        print_ascii(attempt)
    print(sum(attempt))


def decrypt(nums, ds):
    dnums = list()
    index = 0
    for n in nums:
        dn = n ^ ord(ds[index])
        if dn < 32 or dn > 126:
            return False
        dnums.append(dn)
        index = (index + 1) % 3
    return dnums




def print_ascii(nums):
    sentance = ''
    for n in nums:
        sentance += chr(n)
    print sentance


def spiral_primes():
    total = 1
    current = 1
    current_side = 1
    prime_count = 0.0
    total_count = 1.0
    while True:
        current_side += 2
        for j in range(4):
            current += current_side - 1
            if et.is_prime(current):
                prime_count += 1
            total_count += 1
        if prime_count / total_count < 0.1:
            break
    return current_side


def root_converg():
    num = 1
    den = 2
    count = 0
    for i in range(1000):
        num += den
        if len(str(num)) > len(str(den)):
            count += 1
        num, den = den, num + den
    return count



def power_digit_sum():
    max_sum = 0
    for i in range(1, 100):
        for j in range(1, 100):
            num = i**j
            num_sum = sum([int(x) for x in str(num)])
            if num_sum > max_sum:
                max_sum = num_sum
    return max_sum


def lychrel():
    count = 0
    for i in range(1, 10000):
        num = i
        while num < 9:
            num = num + int(str(num)[::-1])
        found_pal = False
        while num < 10000:
            num = num + int(str(num)[::-1])
            if et.is_palindrome(num):
                found_pal = True
                break
        if found_pal:
            continue
        for j in range(50):
            num = num + int(str(num)[::-1])
            if et.is_palindrome(num):
                found_pal = True
                break
        if not found_pal:
            count += 1
    return count


def comb_selects():
    count = 0
    for n in range(23, 101):
        r = n / 2
        count += (n % 2) + 1
        r += (n % 2) + 1
        while choose(n, r) > 1000000:
            count += 2
            r += 1
    return count


def choose(n, r):
    nf = math.factorial(n)
    rf = math.factorial(r)
    nrf = math.factorial(n - r)
    return nf/(rf*nrf)


def permuted_multiples():
    current = 1
    while True:
        match = True
        cur_set = set(str(current))
        for i in range(2,7):
            if cur_set != set(str(current * i)):
                match = False
                break
        if match:
            return current
        current += 1


def prime_digit_replacement():
    primes = et.prime_sieve(9999999)[25:]
    chars = '0123456789'
    for p in primes:
        count = {}
        for s in str(p):
            if count.has_key(s):
                count[s] += 1
            else:
                count[s] = 1
        for key in count:
            if count[key] > 1:
                not_prime = 0
                for c in chars:
                    sp = str(p)
                    np = int(sp.replace(key, c))
                    if len(str(np)) != len(sp):
                        not_prime += 1
                        continue
                    if not et.is_prime(np):
                        not_prime += 1
                    if not_prime > 3:
                        break
                if not_prime < 3:
                    return p


def consecutive_prime_sum():
    primes = et.prime_sieve(1000000)
    max_count = 0
    found_prime = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if j - i < max_count:
                continue
            sp = sum(primes[i:j])
            if sp >= 1000000:
                break
            if sp in primes:
                max_count = j - i
                found_prime = sp
    return found_prime, max_count


def prime_permuts():
    def get_length_4_primes(primes):
        return [x for x in primes if len(str(x)) == 4]

    def build_match_dict(primes):
        m = {}
        for i in primes:
            si = str(i)
            if len(si) != 4:
                continue
            key = ''.join(sorted(list(si)))
            if not m.has_key(key):
                m[key] = list()
            m[key].append(i)
        t = {}
        for k in m:
            if len(m[k]) >= 3:
                t[k] = m[k]
        return t

    def equal_diffs(nums):
        d = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if not d.has_key(diff):
                    d[diff] = set()
                d[diff].add(i)
                d[diff].add(j)
        ed = {}
        for k in d:
            if len(d[k]) < 3:
                continue
            l = list()
            for i in d[k]:
                l.append(nums[i])
            ed[k] = l
        return ed


    primes = get_length_4_primes(et.prime_sieve(10000))
    matches = build_match_dict(primes)
    l = list()
    for key in matches:
        nums = matches[key]
        diff_dict = equal_diffs(nums)
        l.append(diff_dict)
    return l


def four_prime_factors():
    i = 0
    num = 1
    while i < 4:
        if len(set(prime_factor_integer(num))) == 4:
            i += 1
        else:
            i = 0
        num += 1
    return num - 4


def goldbach_other():
    primes = et.prime_sieve()
    dsquares = [2*(x**2) for x in range(1, 10**5 + 1)]
    for i in range(9, 10**5, 2):
        if i in primes:
            continue
        if not check_match(i, primes, dsquares):
            return i


def check_match(num, primes, dsquares):
    for j in primes:
        if j > num:
            return False
        for k in dsquares:
            if j + k == num:
                return True
            if j + k > num:
                break


def tri_pent_hex():
    t = 286
    p = 166
    h = 143
    while True:
        tn = tri(t)
        pn = pent(p)
        hn = hexag(h)
        if tn == pn and pn == hn:
            return tn
        low = min(tn, pn, hn)
        if low == tn:
            t += 1
        if low == pn:
            p += 1
        if low == hn:
            h += 1


def small_diff_pentagonal():
    pn = pentagonal_numbers(5000)
    sd = -1
    for i in range(len(pn)):
        for j in range(i + 1, len(pn)):
            p1 = pn[i]
            p2 = pn[j]
            if p1 + p2 in pn and p2 - p1 in pn:
                if sd == -1 or p2 - p1 < sd:
                    sd = p2 - p1
    return sd


def pentagonal_numbers(count=100):
    numbers = list()
    for i in range(1, count + 1):
        numbers.append(pent(i))
    return numbers


pent = lambda(x): x*(3*x-1)/2
tri = lambda(x): x*(x+1)/2
hexag = lambda(x): x*(2*x-1)


def substring_divisiblity():
    symbols = '0123456789'
    current = list('1023456789')
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    while increment_last_symbol(current, symbols):
        while len(current) < len(symbols):
            append_symbol(current, symbols)
        match = True
        for i in range(7):
            if not int(''.join(current)[i+1:i+4]) % primes[i] == 0:
                match = False
                break
        if match:
            total += int(''.join(current))
    return total


def coded_triangle_numbers():
    tri_count = 0
    tn = triangle_numbers()
    temp = open('words.txt').readline().split(',')
    words = list()
    for i in temp:
        words.append(i[1:-1])
    for w in words:
        wt = sum(ord(j)-64 for j in w)
        if wt in tn:
            tri_count += 1
    return tri_count


def triangle_numbers(count=100):
    numbers = list()
    for i in range(1, count + 1):
        numbers.append(int(.5 * i * (i + 1)))
    return numbers


def pandigital_prime():
    symbols = '1234567'
    products = set()
    max_prime = 0
    while symbols:
        current = list(symbols)
        while increment_last_symbol(current, symbols):
            while len(current) < len(symbols):
                append_symbol(current, symbols)
            if et.is_prime(int(''.join(current))):
                max_prime = int(''.join(current))
        if max_prime > 0:
            return max_prime
        symbols = symbols[:-1]


def champ_constant():
    location = 0
    next_match = 1
    current = 0
    product = 1
    while next_match < 10**6:
        current += 1
        location += len(str(current))
        if location >= next_match:
            diff = location - next_match
            if diff == 0:
                product *= int(str(current)[-1:])
                next_match *= 10
            else:
                product *= int(str(current)[-(diff + 1):-diff])
                next_match *= 10
    return product


def integer_right_triangles(max_perimeter=1000):
    int_triangles = dict()
    for a in range(max_perimeter/2):
        for b in range(max_perimeter - a - 1):
            c2 = a**2 + b**2
            c = math.sqrt(c2)
            if c == int(c):
                p = a + b + c
                if p < max_perimeter:
                    if not int_triangles.has_key(p):
                        int_triangles[p] = list()
                    int_triangles[p].append((a, b, c))
    most = 0
    p = 0
    for key in int_triangles:
        count = len(int_triangles[key])
        if count > most:
            most = count
            p = key
    return p, most


def pandigital_multiple():
    i = 9999
    largest = 0
    while i > 0:
        j = 0
        concat = ''
        while len(concat) <9:
            j += 1
            concat += str(i*j)
        if '0' in concat:
            i -= 1
            continue
        if len(concat) == 9 and len(set(concat)) == 9:
            if largest < int(concat):
                largest = int(concat)
        i -= 1
    return largest


def truncate_primes():
    print 'generating primes...'
    primes = list_primes(max_value=10**6)
    print 'processing primes...'
    tp = set()
    for p in primes:
        if p < 10:
            continue
        sp = str(p)
        is_tp = True
        for i in range(1, len(sp)):
            if int(sp[i:]) not in primes or int(sp[:i*-1]) not in primes:
                is_tp = False
        if is_tp:
            tp.add(p)
    return tp


def double_base_palindromes():
    total = 0
    for i in range(1, 10**6, 2):
        if is_numeric_palindrome(i) and is_numeric_palindrome(bin(i)[2:]):
            total += i
    return total


def circular_primes():
    primes = list_primes(max_value=1000000)
    circular_primes = set()
    for i in primes:
        si = str(i)
        circle_i = get_circle_set(i)
        matching_primes = set([i for i in circle_i if i in primes])
        if circle_i == matching_primes:
            circular_primes = circular_primes.union(circle_i)
    return len(circular_primes)


def get_circle_set(num):
    circle_set = set()
    snum = str(num)
    for i in range(len(snum)):
        circle_set.add(int(snum[i:] + snum[:i]))
    return circle_set


def digit_factorials():
    found_total = 0
    for i in range(10, 2500000):
        si = str(i)
        fac_total = 0
        for c in si:
            fac_total += math.factorial(int(c))
        if fac_total == i:
            found_total += i
            print i
    print found_total


def digit_cancel_fraction():
    fractions = list()
    for i in range(11, 100):
        for j in range(11, i):
            si = str(i)
            j1, j2 = str(j)
            if j1 in si:
                value = check_fractions((j, i), (int(j2), int(si[(si.index(j1)+1)%2])))
                if value:
                    fractions.append(value)
            if j2 in si:
                value = check_fractions((j, i), (int(j1), int(si[(si.index(j2)+1)%2])))
                if value:
                    fractions.append(value)


def check_fractions(f1, f2):
    if f2[1] == 0:
        return False
    if f1[1] % 10 == 0:
        return False
    if f1[0]/float(f1[1]) == f2[0]/float(f2[1]):
        allf = f1 + f2
        print '%d/%d == %d/%d' % allf
        return f1

def pandigital_products():
    symbols = '123456789'
    current = list('123456789')
    products = set()
    while increment_last_symbol(current, symbols):
        while len(current) < len(symbols):
            append_symbol(current, symbols)
        for i in range(1, 5):
            for j in range(i+1, 6):
                m1 = int(''.join(current[:i]))
                m2 = int(''.join(current[i:j]))
                prod = int(''.join(current[j:]))
                if m1 * m2 == prod:
                    products.add(prod)
    return sum(products)


def coin_sums():
    count = 0
    for l2 in range(2):
        for l in range(3-(l2*2)):
            for p50 in range(5-(l2*4)-(l*2)):
                for p20 in range(11-(l2*10)-(l*5)-(int(math.ceil(p50*2.5)))):
                    for p10 in range(21-(l2*20)-(l*10)-(p50*5)-(p20*2)):
                        for p5 in range(41-(l2*40)-(l*20)-(p50*10)-(p20*4)-(p10*2)):
                            for p2 in range(101-(l2*100)-(l*50)-(p50*25)-(p20*10)-(p10*5)-(int(math.ceil(p5*2.5)))):
                                count += 1
    return count


def fifth_powers(start, end):
    numbers = list()
    for i in range(start, end):
        if i == sum(int(j)**5 for j in str(i)):
            numbers.append(i)
    return numbers


def distinct_powers(max_a_b):
    terms = set()
    for a in range(2, max_a_b + 1):
        for b in range(2, max_a_b + 1):
            terms.add(a**b)
    return len(terms)


def spiral_sums(max_side_length):
    total = 1
    current = 1
    for i in range(2, max_side_length, 2):
        for j in range(4):
            current += i
            total += current
    return total


def quadratic_primes(max_a_b):
    primes = list_primes(max_value=50000)
    max_primes = 0
    max_a = 0
    max_b = 0
    for a in range((max_a_b - 1) * -1, max_a_b):
        for b in range(max_a_b):
            n = 0
            while True:
                val = n**2 + (a*n) + b
                if val > primes[-1]:
                    print 'Failed value: %d, higher than max prime' % val
                    return
                elif val in primes:
                    n += 1
                else:
                    if n - 1 > max_primes:
                        max_primes = n - 1
                        max_a = a
                        max_b = b
                    break
    return max_primes, max_a, max_b


def longest_repeating(max_num):
    longest_num = 0
    longest_length = 0
    for i in range(1, max_num + 1):
        p = 1
        q = i
        terms = list()
        while p != 0:
            if p < q:
                p = p * 10
            else:
                n = p/q
                p = p%q
                if (n, p) in terms:
                    length = len(terms) - terms.index((n, p))
                    if length > longest_length:
                        longest_num = i
                        longest_length = length
                    p = 0
                else:
                    terms.append((n, p))
    return longest_num, longest_length


def fib_length(length):
    f1 = 1
    f2 = 1
    term = 2
    while len(str(f2)) < length:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        term += 1
    return term, f2


def lexographical_index(symbols, index):
    count = 0
    current = list()
    last_found = current
    symbol_count = len(symbols)
    while count < index:
        while len(current) < symbol_count:
            append_symbol(current, symbols)
        count += 1
        last_found = list(current)
        increment_last_symbol(current, symbols)
    return last_found


def append_symbol(current, symbols):
    for s in symbols:
        if s not in current:
            current.append(s)
            return current


def increment_last_symbol(current, symbols):
    if not current:
        return
    last_s = current.pop()
    for i in range(symbols.index(last_s) + 1, len(symbols)):
        if symbols[i] not in current:
            current.append(symbols[i])
            return current
    return increment_last_symbol(current, symbols)


def non_abundant_sums():
    min_abundant_sum = 28123
    total = 0
    abundant_sums = {}
    abundant_numbers = list()
    for i in range(1, min_abundant_sum):
        if not abundant_sums.has_key(i):
            total += i
        factor_sum = sum(factor_integer(i)) - i
        if factor_sum > i:
            abundant_numbers.append(i)
            for num in abundant_numbers:
                abundant_sums[num+i] = 1
    return total


def name_value(file_name):
    temp = open(file_name).readline().split(',')
    names = list()
    for i in temp:
        names.append(i[1:-1])
    names.sort()
    total = 0
    for i in range(len(names)):
        total += sum(ord(j)-64 for j in names[i]) * (i + 1)
    return total


def amiacble_number_sum(max_num):
    total_sum = 0;
    for i in range(1, max_num + 1):
        item_sum = sum(factor_integer(i)) - i
        if item_sum > i and sum(factor_integer(item_sum)) - item_sum == i:
            total_sum += i
            total_sum += item_sum
    return total_sum


def count_sundays():
    day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 7
    year = 1901
    day = 2
    sundays = 0
    while year <= 2000:
        for i in range(len(day_count)):
            if day == 0:
                sundays += 1
            day += day_count[i] % 7
            if i == 1 and year % 4 == 0 and year != 2000:
                day += 1
            day = day % 7
        year += 1
    return sundays


def max_path_sum(file_name):
    lines = list()
    for line in reversed(open(file_name).readlines()):
        int_line = list()
        for item in line.split():
            int_line.append(int(item))
        lines.append(int_line)
    for i in range(len(lines)-1):
        for j in range(len(lines[i])-1):
            lines[i+1][j] += max(lines[i][j], lines[i][j+1])
    return lines[-1]


def number_letter_count(num):
    total = 0
    for i in range(1, num + 1):
        output = str(i) + " - "
        if i >= 1000:
            total += len(singles[i/1000])
            total += len('thousand')
        if i >= 100 and i % 1000 != 0:
            total += len(singles[int(str(i)[-3])])
            total += len('hundred')
            if i % 100 != 0:
                total += len('and')
        num = i % 100
        if num > 19:
            total += len(tens[int(str(i)[-2])])
        elif num > 10 and num < 20:
            total += len(teens[num-10])
            continue
        if num == 10:
            total += len(tens[1])
        total += len(singles[num%10])
    return total


def lattice_paths(size):
    current = list()
    current.append(1)
    while len(current) <= size:
        n = list()
        n.append(current[0])
        for i in range(len(current) - 1):
            n.append(current[i] + current[i+1])
        n.append(current[-1])
        current = n
    while len(current) > 1:
        n = list()
        for i in range(len(current) - 1):
            n.append(current[i] + current[i+1])
        current = n
    return n[0]


def longest_collatz_sequence(max_num):
    count_map = {}
    count_map[1] = 1
    largest_chain = 1
    largest_chain_length = 1
    for i in range(2, max_num + 1):
        num = i
        chain = list()
        while not num in count_map:
            chain.append(num)
            if num % 2:
                num = 3*num + 1
            else:
                num = num / 2
        chain_count = count_map[num]
        for item in chain[::-1]:
            chain_count = chain_count + 1
            count_map[item] = chain_count
        if chain_count > largest_chain_length:
            largest_chain_length = chain_count
            largest_chain = i
    return largest_chain, largest_chain_length


def print_collatz_sequence(num):
    while num > 1:
        print num
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1
    print num


def large_sum(number_list, digit_count):
    number_size = len(number_list[0])
    digit_sums = list()
    total = 0;
    for number in number_list:
        total = total + int(number[-1])
    total = str(total)
    for i in range(1, number_size):
        cur_sum = 0
        for number in number_list:
            cur_sum = cur_sum + int(number[(i+1) * -1])
        part = int(total[:i*-1]) + cur_sum
        total = str(part) + total[i*-1:]
    return total[:digit_count]


def triangle_divisors(num_divisors):
    index = 1
    cur_number = 1
    factors = factor_integer(cur_number)
    while len(factors) < num_divisors:
        index = index + 1
        cur_number = cur_number + index
        factors = factor_integer(cur_number)
    return cur_number


def factor_integer(number):
    factors = list()
    for i in range(1, int(math.sqrt(number)) + 1):
        if number%i == 0:
            factors.append(i)
            if number/i != i:
                factors.append(number/i)
    return factors


def largest_product_grid(grid, row_size, segment_size):
    grid_size = len(grid)
    if grid_size % row_size != 0:
        return "Failed: bad grid size"
    row_count = grid_size / row_size
    largest = 0
    match = ()
    # horizontal check
    for i in range(row_size - segment_size + 1):
        for j in range(row_count):
            start = (j * row_size) + i
            end = start + segment_size
            product = reduce(operator.mul, grid[start:end], 1)
            if product > largest:
                largest = product
                match = grid[start:end]
    # vertical check
    for i in range(row_size):
        for j in range(row_count - segment_size + 1):
            group = list()
            for k in range(segment_size):
                index = ((j+k)*row_size) + i
                group.append(grid[index])
            product = reduce(operator.mul, group, 1)
            if product > largest:
                largest = product
                match = group
    # diagonal check down left to right
    for i in range(row_size - segment_size + 1):
        for j in range(row_count - segment_size + 1):
            group = list()
            for k in range(segment_size):
                index = ((j+k)*row_size) + i + k
                group.append(grid[index])
            product = reduce(operator.mul, group, 1)
            if product > largest:
                largest = product
                match = group
    # diagonal check up left to right
    for i in range(segment_size - 1, row_size):
        for j in range(row_count - segment_size + 1):
            group = list()
            for k in range(segment_size):
                index = ((j+k)*row_size) + i - k
                group.append(grid[index])
            product = reduce(operator.mul, group, 1)
            if product > largest:
                largest = product
                match = group
    return largest, match


def pythagorean_triplet(total_sum):
    for a in range(1, total_sum/2):
        for b in range(a+1, ((total_sum-a)/2) + 1):
            c = total_sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return "No match found"


def largest_product_in_series(ns):
    max = 0;
    max_values = ()
    for i in range(len(ns) - 5):
        a, b, c, d, e = ns[i:i+5]
        val = int(a)*int(b)*int(c)*int(d)*int(e)
        if val > max:
            max = val
            max_values = (a, b, c, d, e)
    return max, max_values


def list_primes(max_count=None, max_value=None):
    if max_count == None and max_value == None:
        return "Must supply at least one of max_count or max_value"
    found_primes = list()
    found_primes.append(2)
    i = 3
    keep_searching = True
    while keep_searching:
        is_prime = True
        for prime in found_primes:
            if i % prime == 0:
                is_prime = False
                break;
        if is_prime:
            found_primes.append(i)
        i = i + 1
        if max_count != None and len(found_primes) >= max_count:
            keep_searching = False
        if max_value != None and i >= max_value:
            keep_searching = False
    return found_primes


def diff_of_squares(num):
    #compute sum of squares
    sum_square = 2*(num**3) + 3*(num**2) + num
    sum_square = sum_square / 6
    #compute square of sums
    square_sum = (num**2 + num) / 2
    square_sum = square_sum**2
    return square_sum - sum_square


def min_divisible_by(max):
    numbers = range(1, max + 1)
    current = max
    found = False
    while not found:
        found = True
        for num in numbers:
            if current % num != 0:
                current = current + 1
                found = False
                break;
    return current


def next_candidate(num):
    while not is_numeric_palindrome(num):
        num = num - 1
    factors = factor_integer(num)
    if len(str(factors[-1])) <= 3:
        return factors, num
    else:
        return next_candidate(num - 1)


def is_numeric_palindrome(num):
    num_string = str(num)
    half = len(num_string) / 2
    for i in range(half):
        if num_string[i] != num_string[(i + 1) * -1]:
            return False
    return True


def prime_factor_integer(num):
    factors = list()
    current_factor = 2
    while (current_factor < num):
        if num % current_factor == 0:
            num = num / current_factor
            factors.append(current_factor)
        else:
            current_factor = current_factor + 1
    factors.append(num)
    return factors


def sum_even_fibonacci(max):
    total = 0
    fib_1 = 1
    fib_2 = 1
    while fib_2 < max:
        new_fib = fib_1 + fib_2
        if new_fib % 2 == 0:
            total = total + new_fib
        fib_1 = fib_2
        fib_2 = new_fib
    return total

singles = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
teens = ('', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

prob_11_grid = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,
                49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0,
                81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,
                52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,
                22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,
                24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,
                32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,
                67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,
                24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,
                21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,
                78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,
                16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,
                86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,
                19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,
                4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,
                88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,
                4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,
                20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,
                20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,
                1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48,]

prob_13_numbers = ('37107287533902102798797998220837590246510135740250',
'46376937677490009712648124896970078050417018260538',
'74324986199524741059474233309513058123726617309629',
'91942213363574161572522430563301811072406154908250',
'23067588207539346171171980310421047513778063246676',
'89261670696623633820136378418383684178734361726757',
'28112879812849979408065481931592621691275889832738',
'44274228917432520321923589422876796487670272189318',
'47451445736001306439091167216856844588711603153276',
'70386486105843025439939619828917593665686757934951',
'62176457141856560629502157223196586755079324193331',
'64906352462741904929101432445813822663347944758178',
'92575867718337217661963751590579239728245598838407',
'58203565325359399008402633568948830189458628227828',
'80181199384826282014278194139940567587151170094390',
'35398664372827112653829987240784473053190104293586',
'86515506006295864861532075273371959191420517255829',
'71693888707715466499115593487603532921714970056938',
'54370070576826684624621495650076471787294438377604',
'53282654108756828443191190634694037855217779295145',
'36123272525000296071075082563815656710885258350721',
'45876576172410976447339110607218265236877223636045',
'17423706905851860660448207621209813287860733969412',
'81142660418086830619328460811191061556940512689692',
'51934325451728388641918047049293215058642563049483',
'62467221648435076201727918039944693004732956340691',
'15732444386908125794514089057706229429197107928209',
'55037687525678773091862540744969844508330393682126',
'18336384825330154686196124348767681297534375946515',
'80386287592878490201521685554828717201219257766954',
'78182833757993103614740356856449095527097864797581',
'16726320100436897842553539920931837441497806860984',
'48403098129077791799088218795327364475675590848030',
'87086987551392711854517078544161852424320693150332',
'59959406895756536782107074926966537676326235447210',
'69793950679652694742597709739166693763042633987085',
'41052684708299085211399427365734116182760315001271',
'65378607361501080857009149939512557028198746004375',
'35829035317434717326932123578154982629742552737307',
'94953759765105305946966067683156574377167401875275',
'88902802571733229619176668713819931811048770190271',
'25267680276078003013678680992525463401061632866526',
'36270218540497705585629946580636237993140746255962',
'24074486908231174977792365466257246923322810917141',
'91430288197103288597806669760892938638285025333403',
'34413065578016127815921815005561868836468420090470',
'23053081172816430487623791969842487255036638784583',
'11487696932154902810424020138335124462181441773470',
'63783299490636259666498587618221225225512486764533',
'67720186971698544312419572409913959008952310058822',
'95548255300263520781532296796249481641953868218774',
'76085327132285723110424803456124867697064507995236',
'37774242535411291684276865538926205024910326572967',
'23701913275725675285653248258265463092207058596522',
'29798860272258331913126375147341994889534765745501',
'18495701454879288984856827726077713721403798879715',
'38298203783031473527721580348144513491373226651381',
'34829543829199918180278916522431027392251122869539',
'40957953066405232632538044100059654939159879593635',
'29746152185502371307642255121183693803580388584903',
'41698116222072977186158236678424689157993532961922',
'62467957194401269043877107275048102390895523597457',
'23189706772547915061505504953922979530901129967519',
'86188088225875314529584099251203829009407770775672',
'11306739708304724483816533873502340845647058077308',
'82959174767140363198008187129011875491310547126581',
'97623331044818386269515456334926366572897563400500',
'42846280183517070527831839425882145521227251250327',
'55121603546981200581762165212827652751691296897789',
'32238195734329339946437501907836945765883352399886',
'75506164965184775180738168837861091527357929701337',
'62177842752192623401942399639168044983993173312731',
'32924185707147349566916674687634660915035914677504',
'99518671430235219628894890102423325116913619626622',
'73267460800591547471830798392868535206946944540724',
'76841822524674417161514036427982273348055556214818',
'97142617910342598647204516893989422179826088076852',
'87783646182799346313767754307809363333018982642090',
'10848802521674670883215120185883543223812876952786',
'71329612474782464538636993009049310363619763878039',
'62184073572399794223406235393808339651327408011116',
'66627891981488087797941876876144230030984490851411',
'60661826293682836764744779239180335110989069790714',
'85786944089552990653640447425576083659976645795096',
'66024396409905389607120198219976047599490197230297',
'64913982680032973156037120041377903785566085089252',
'16730939319872750275468906903707539413042652315011',
'94809377245048795150954100921645863754710598436791',
'78639167021187492431995700641917969777599028300699',
'15368713711936614952811305876380278410754449733078',
'40789923115535562561142322423255033685442488917353',
'44889911501440648020369068063960672322193204149535',
'41503128880339536053299340368006977710650566631954',
'81234880673210146739058568557934581403627822703280',
'82616570773948327592232845941706525094512325230608',
'22918802058777319719839450180888072429661980811197',
'77158542502016545090413245809786882778948721859617',
'72107838435069186155435662884062257473692284509516',
'20849603980134001723930671666823555245252804609722',
'53503534226472524250874054075591789781264330331690')
