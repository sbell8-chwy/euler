def solve():
    comes_after = []
    needed_numbers = set()
    for i in range(10):
        comes_after.append(set())
    for line in open('keylog.txt').read().splitlines():
        digits = [int(x) for x in line]
        for i in range(len(digits)):
           comes_after[digits[i]].update(digits[:i])
           needed_numbers.add(digits[i])
    result = ''
    while needed_numbers:
        found_number = False
        for n in needed_numbers:
            if not comes_after[n]:
                found_number = True
                result += str(n)
                for s in comes_after:
                    s.discard(n)
                break
        if not found_number:
            print needed_numbers
            print comes_after
            break
        needed_numbers.remove(int(result[-1]))
    return result
