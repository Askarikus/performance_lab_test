import sys


def is_in_circle(x, y, r, d_x, d_y):
    result = -1
    delta = (x - d_x) ** 2 + (y - d_y) ** 2
    if delta < r ** 2:
        result = 1  # inside
    elif delta > r ** 2:
        result = 2  # outside
    elif delta == r ** 2:
        result = 0  # on circle
    return result


if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as start_radius_file, open(sys.argv[2]) as dots_file:
            x, y = [float(i) for i in start_radius_file.readline().split()]
            r = float(start_radius_file.readline())
            dots_list = [(float(j), float(k)) for j, k in [i.strip('\n').split() for i in dots_file.readlines()]]
            for dots in dots_list:
                print(is_in_circle(x, y, r, dots[0], dots[1]))
