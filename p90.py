squares = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)];

def bruteforce():
    result = 0;
    combinations = all_combinations(6, 10)
    for i in range(len(combinations)):
        if combinations[i][0] != 0:
            break;
        for j in range(i+1, len(combinations)):
            if is_valid_combo(combinations[i], combinations[j]):
                result = result + 1;
    return result;

def all_combinations(k, n):
    combinations = [];
    comb = range(k);
    while True:
        combinations.append(comb);
        comb = list(comb);
        if combinations[-1][k-1] == 9: combinations[-1][k-1] = 6;
        i = k - 1;
        comb[i] = comb[i] + 1;
        while i > 0 and comb[i] >= n - k + 1 + i:
            i = i - 1;
            comb[i] = comb[i] + 1;
        if comb[0] > n-k:break
        for j in range(i + 1, k):
            comb[j] = comb[j - 1] + 1;
    return combinations;

def is_valid_combo(d1, d2):
    combs = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (6,4), (8,1)];
    valid = True;
    for i in range(len(combs)):
        if combs[i][0] in d1 and combs[i][1] in d2: continue;
        if combs[i][0] in d2 and combs[i][1] in d1: continue;
        valid = False;
        break;
    return valid;


''' Can't seem to get the below to work. Trying to enumerate possibilities by squares
    then fill in unused die faces.'''
def get_count():
    count = 0;
    options = compute_all_dice_options();
    options = fill_out_dice(options);
    options = filter_duplicates(options);
    '''
    for option in options:
        option_count = 1;
        if len(option[0]) == 5:
            option_count = 5;
        if len(option[0]) == 4:
            option_count = 15;
        if len(option[1]) == 5:
            option_count = option_count * 5;
        if len(option[1]) == 4:
            option_count = option_count * 15;
        count = count + option_count;
        '''
    return len(options);

def filter_duplicates(options):
    new_options = [];
    for option in options:
        if option not in new_options and (option[1], option[0]) not in new_options:
            new_options.append(option);
    return new_options;

def compute_all_dice_options():
    dice_options = [((0,), (1,))];
    for square in squares[1:]:
        dice_options = add_posibilities(dice_options, square);

    return dice_options;

def fill_out_dice(dice_options):
    full_dice = [];
    for option in dice_options:
        full1 = fill_single_die(option[0]);
        full2 = fill_single_die(option[1]);
        for die1 in full1:
            for die2 in full2:
                full_dice.append((die1, die2));
    return full_dice;

def fill_single_die(die):
    if len(die) == 6:
        return [sorted(die)];
    if len(die) == 5:
        full_dice = [];
        for i in range(10):
            if i not in die:
                full_die = die + (i,);
                full_dice.append(sorted(full_die));
        return full_dice;
    if len(die) == 4:
        full_dice = [];
        for i in range(10):
            if i not in die:
                for j in range(i + 1, 10):
                    if j not in die:
                        full_die = die + (i, j);
                        full_dice.append(sorted(full_die));
        return full_dice;

def add_posibilities(dice_options, square):
    new_dice_options = [];
    first_digit = square[0];
    second_digit = square[1];
    for dice in dice_options:
        new_dice = append_digits(dice, first_digit, second_digit);
        append_dice(new_dice_options, new_dice);

        if first_digit == 6 or first_digit == 9:
            new_dice = append_digits(dice, 6 if first_digit == 9 else 9, second_digit);
            append_dice(new_dice_options, new_dice);

        new_dice = append_digits(dice, second_digit, first_digit);
        append_dice(new_dice_options, new_dice);

        if second_digit == 6 or second_digit == 9:
            new_dice = append_digits(dice, first_digit, 6 if second_digit == 9 else 9);
            append_dice(new_dice_options, new_dice);

    return new_dice_options;

def append_dice(dice_options, new_dice):
    if new_dice != None:
        dice_options.append(new_dice);

def append_digits(dice, first, second):
    d1 = dice[0];
    d2 = dice[1];
    if first not in d1:
        d1 = d1 + (first,)
    if second not in d2:
        d2 = d2 + (second,)
    if len(d1) > 6 or len(d2) > 6:
        return None;
    return (d1, d2);
