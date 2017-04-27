
def count_triangles(min, max):
    count = 0;
    x = (0, 0);
    points = generate_points(min, max);
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if check_right_triangle(x, points[i], points[j]):
                count = count + 1;
    return count;

def generate_points(min, max):
    points = [];
    for i in range(min, max + 1):
        for j in range(min, max + 1):
            points.append((i, j));
    return points;

def check_right_triangle(x, y, z):
    a = calc_square_line_length(x, y);
    b = calc_square_line_length(y, z);
    c = calc_square_line_length(z, x);
    if a == 0 or b == 0 or c == 0:
        return False;
    sides = sorted((a, b, c))
    return sides[0] + sides[1] == sides[2];

def calc_square_line_length(a, b):
    x = (a[0] - b[0])**2;
    y = (a[1] - b[1])**2;
    return x + y;
