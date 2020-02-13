# Greatest product of 4 in a line on grid of numbers
import sys
import numpy as np
from functools import reduce
from operator import mul


def read_int_matrix():
    arr = []
    for line in sys.stdin:
        arr.append(list(map(int, line.split())))
    return arr


if __name__ == "__main__":
    adj = int(4)
    m = read_int_matrix()
    mm = np.array(m)
    ans = set()
    for row in range(len(m)):
        for col in range(len(m[row])):
            box = mm[row : row + adj, col : col + adj]
            vecs = box.diagonal(), box[0, :], box[:, 0], box[::-1].diagonal()
            sums = box.diagonal(), box[0, :], box[:, 0], box[::-1].diagonal()
            q = [reduce(mul, j, 1) for j in vecs]
            for i in q:
                ans.add(i)
    print(max(ans))
