import sys


class Node:
    cost = 0
    distance = sys.maxint


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
    root = parse_file('matrix_82.txt')
    
