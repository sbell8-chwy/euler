import sys


class Node:
    cost = 0
    distance = sys.maxint

    def __repr__(self):
        return '[' + str(self.cost).zfill(6) + ',' + str(self.distance).zfill(6) + ']'


def parse_file(filename):
    matrix = []
    for line in open(filename).read().splitlines():
        matrix.append([])
        for n in line.split(','):
            new_node = Node()
            new_node.cost = int(n)
            matrix[-1].append(new_node)
    return matrix


def solve():
    matrix = parse_file('matrix_82.txt')
    #matrix = parse_file('matrix_small.txt')
    COLUMN_COUNT = len(matrix)
    column = COLUMN_COUNT - 1
    while column >= 0:
        row = 0
        ROW_COUNT = len(matrix[column])
        while row < ROW_COUNT:
            #Load values for last column
            if column == COLUMN_COUNT - 1:
                matrix[row][column].distance = matrix[row][column].cost
                row += 1
                continue
            current_cost = matrix[row][column].cost
            move_right = current_cost + matrix[row][column + 1].distance
            move_up = sys.maxint
            if row > 0:
                move_up = current_cost + matrix[row - 1][column].distance
            move_down = sys.maxint
            if row < ROW_COUNT - 1:
                column_cost = current_cost
                check_row = row + 1
                while check_row < ROW_COUNT:
                    column_cost += matrix[check_row][column].cost
                    if column_cost != min(move_right, move_up, column_cost):
                        break
                    move_down = min(column_cost + matrix[check_row][column + 1].distance, move_down)
                    check_row += 1
            matrix[row][column].distance = min(move_right, move_up, move_down)
            row += 1
        column -= 1
    return matrix


def get_lowest_cost(matrix):
    best_cost = sys.maxint
    for row in matrix:
        best_cost = min(row[0].distance, best_cost)
    return best_cost

def print_matrix(matrix):
    f = open('matrix_out.txt', 'w+')
    for line in matrix:
        print >>f, line
