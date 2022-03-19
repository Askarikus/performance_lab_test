import sys
from itertools import cycle


def generator(m, n):
    k = 0
    for index, element in enumerate(cycle(range(1, m + 1))):
        if (index + 1 + k) % n == 0:
            k += 1
            yield element


def pathway(m, n):
    sequence = [1]
    for i in generator(m, n):
        if i == 1:
            break
        sequence.append(i)
    print(''.join(str(j) for j in sequence))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        pathway(int(sys.argv[1]), int(sys.argv[2]))
