import random

cc_pos = 0
chance_pos = 0

def cc(curr_pos):
    global cc_pos
    card = cc_pos
    cc_pos = (cc_pos + 1) % 16
    if card == 0:
        return 0
    if card == 1:
        return 10
    return curr_pos

def chance(curr_pos):
    global chance_pos
    card = chance_pos
    chance_pos = (chance_pos + 1) % 16
    straight_jumps = [0, 10, 11, 24, 39, 5]
    if card < 6:
        return straight_jumps[card]
    if card == 7 or card == 8:
        if curr_pos == 7:
            return 15
        if curr_pos == 22:
            return 25
        if curr_pos == 36:
            return 5
    if card == 8:
        if curr_pos == 22:
            return 28
        return 12
    if card == 9:
        return curr_pos - 3
    return curr_pos


def index_top_three(board):
    one = (0, 0)
    two = (0, 0)
    three = (0, 0)
    for i in range(len(board)):
        if board[i] > one[1]:
            three = two
            two = one
            one = (i, board[i])
        elif board[i] > two[1]:
            three = two
            two = (i, board[i])
        elif board[i] > three[1]:
            three = (i, board[i])
    return [one, two, three]


def solve(sample=10**7, dice_face=6):
    i = 0
    position = 0
    board = [0] * 40
    doubles = 0
    while i < sample:
        die_1 = random.randint(1, dice_face)
        die_2 = random.randint(1, dice_face)
        if die_1 == die_2:
            doubles += 1
        else:
            doubles = 0
        if doubles > 2:
            position = 10
            doubles = 0
        else:
            position = (position + die_1 + die_2) % 40
            if position in (7, 22, 36):
                position = chance(position)
            if position in (2, 17, 33):
                position = cc(position)
            if position == 30:
                position = 10
        board[position] += 1
        i += 1
    return index_top_three(board)
