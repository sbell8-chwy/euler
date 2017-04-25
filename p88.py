import euler_tools
import math
from operator import mul
from sets import Set

def compute_min_product_sum_set(count):
    product_sum_array = compute_product_sum_array(count * 2);
    min_product_sum_set = Set();
    for i in range(2, count + 1):
        min_product_sum_set.add(product_sum_array[i][0]);
    return min_product_sum_set;

def compute_product_sum_array(limit):
    num_array = [2, 2];
    product_sum_solutions = [None] * limit;
    product_sum_solutions[2] = (4, list(num_array));
    num_array = increment_num_array(num_array, limit);
    product = reduce(mul, num_array);
    while product <= limit:
        index = product - sum(num_array) + len(num_array);
        if (product_sum_solutions[index] == None or product_sum_solutions[index][0] > product):
            product_sum_solutions[index] = (product, list(num_array));
        num_array = increment_num_array(num_array, limit);
        product = reduce(mul, num_array);
    return product_sum_solutions;

def increment_num_array(num_array, limit):
    index = len(num_array) - 1;
    num_array[index] = num_array[index] + 1;
    while reduce(mul, num_array) > limit:
        index = index - 1;
        if index == -1:
            return [2] * (len(num_array) + 1);
        num_array[index] = num_array[index] + 1;
        for i in range(index + 1, len(num_array)):
            num_array[i] = num_array[index];
    return num_array;

# Hmmm, slow and not working...
def compute_set_min_product_sums(k_array):
    min_product_sum_set = Set();
    for k in k_array:
        min_product_sum_set.add(compute_min_product_sum(k));
    return min_product_sum_set;

def compute_min_product_sum(count):
    if count == 2:
        return 4;
    num_array = ([1] * (count - 2)) + [2, 2];
    min_product_sum = 9999999;
    while True:
        sum_total = sum(num_array);
        product_total = reduce(mul, num_array);
        if sum_total > product_total:
            num_array[-1] = num_array[-1] + 1;
        elif sum_total < product_total:
            if max(num_array) == 2:
                return min_product_sum;
            roll_up_increment(num_array);
        else: #sum_total == product_total
            if sum_total < min_product_sum:
                min_product_sum = sum_total;
            roll_up_increment(num_array);


def roll_up_increment(num_array):
    limit = max(num_array);
    for i, e in reversed(list(enumerate(num_array))):
        if e >= limit - 1:
            num_array[i] = 2;
            continue;
        num_array[i] = num_array[i] + 1;
        break;
