# Greatest product of 4 in a line on grid of numbers
import sys


def horizntl_product(matrix, adjacent, r, c):
    print("h")
    if r > len(matrix) or c > (len(matrix[r]) - adjacent):
        print("%")
        return 0
    else:
        product = 1
        for offset in range(adjacent):
            product *= int(matrix[r + offset][c])
        return product


def vertical_product(matrix, adjacent, r, c):
    print("v")
    if r > len(matrix):
        return 0
    else:
        product = 1
        for offset in range(adjacent):
            product *= int(matrix[r][c + offset])
        return product


def diagonal_product_right(matrix, adjacent, r, c):
    print("r")
    if r > len(matrix) or c > (len(matrix[r]) - adjacent):
        print("%")
        return 0
    else:
        product = 1
        for offset in range(adjacent):
            product *= int(matrix[r + offset][c + offset])
        return product


def diagonal_product_left(matrix, adjacent, r, c):
    if c < adjacent:
        print("*")
        return 0
    else:
        product = 1
        for offset in range(adjacent):
            product *= int(matrix[r - offset][c - offset])
        return product


def largest_product(matrix, adjacent, r, c):
    return max(
        [
            horizntl_product(matrix, adjacent, r, c),
            vertical_product(matrix, adjacent, r, c),
            diagonal_product_right(matrix, adjacent, r, c),
            diagonal_product_left(matrix, adjacent, r, c),
        ]
    )


def read_int_matrix():
    arr = []
    for line in sys.stdin:
        arr.append(line.split())
    return arr


if __name__ == "__main__":
    adjacent_numbers = int(4)
    m = read_int_matrix()
    all = []
    for row_i in range(0, len(m) + 1 - adjacent_numbers):
        for col_i in range(0, len(m[row_i])):
            all.append(largest_product(m, adjacent_numbers, row_i, col_i))
    print(len(all))
    print(max(all))
