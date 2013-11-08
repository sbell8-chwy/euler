import sys


class Node:
    cost = 0
    distance = sys.maxint
    right = None
    down = None
    up = None
    left = None
    came_from = None
    visited = False


def parse_file(filename):
    root = None
    previous_row = []
    current_row = []
    for line in open(filename).read().splitlines():
        for n in line.split(','):
            new_node = Node()
            new_node.cost = int(n)
            if not root:
                root = new_node
            if current_row:
                current_row[-1].right = new_node
                new_node.left = current_row[-1]
            current_row.append(new_node)
            if previous_row:
                previous_row[len(current_row) - 1].down = new_node
                new_node.up = previous_row[len(current_row) - 1]
        previous_row = current_row
        current_row = []
    return root


def get_next_node(edge):
    best_node = edge[0]
    for node in edge:
        if not node.visited and node.distance < best_node.distance:
            best_node = node
    return best_node


def solve():
    root = parse_file('matrix_83.txt')
    target = None
    edge = []
    edge.append(root)
    root.distance = root.cost
    while edge:
        u = get_next_node(edge)
        edge.remove(u)
        u.visited = True
        if not u.right and not u.down:
            target = u
        for v in [u.right, u.down, u.up, u.left]:
            if not v:
                continue
            alt = u.distance + v.cost
            if alt < v.distance and not v.visited:
                v.distance = alt
                v.came_from = u
                edge.append(v)
    return target.distance
