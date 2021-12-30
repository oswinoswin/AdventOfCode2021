import re
from pprint import pprint

import numpy as np


def first(filename):
    p = re.compile(r'\d+')
    points_list = []
    folds = []
    max_x, max_y = 0, 0
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("fold along"):
                digit = p.findall(line)[-1]
                digit = int(digit)
                direction = 'x' if 'x' in line else 'y'
                folds.append((direction, digit))
                continue
            if line == "\n":
                continue

            x, y = p.findall(line)
            x = int(x)
            y = int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            points_list.append((y, x))

    points = np.zeros((max_y + 1, max_x + 1))
    for point in points_list:
        points[point] = 1

    direction, fold_line = folds[0]

    return make_fold(points, direction, fold_line).sum()


def make_fold(points, direction, fold_line):
    max_y, max_x = points.shape
    if direction == 'y':
        max_dist = max_y - fold_line
        for y in range(max_dist):
            for x in range(max_x):
                if points[fold_line - y, x] == 0:
                    points[fold_line - y, x] = points[fold_line + y, x]
        return points[:fold_line, :]
    else:
        max_dist = max_x - fold_line
        for x in range(max_dist):
            for y in range(max_y):
                if points[y, fold_line - x] == 0:
                    points[y, fold_line - x] = points[y, x + fold_line]
        return points[:, :fold_line]



def second(filename):
    p = re.compile(r'\d+')
    points_list = []
    folds = []
    max_x, max_y = 0, 0
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("fold along"):
                digit = p.findall(line)[-1]
                digit = int(digit)
                direction = 'x' if 'x' in line else 'y'
                folds.append((direction, digit))
                continue
            if line == "\n":
                continue

            x, y = p.findall(line)
            x = int(x)
            y = int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            points_list.append((y, x))

    points = np.zeros((max_y + 1, max_x + 1))
    for point in points_list:
        points[point] = 1
    print(points.shape)
    for direction, fold_line in folds:
        points = make_fold(points, direction, fold_line)
        # print(points)
    print(points.shape)
    for line in points:
        res = ""
        print(res.join(["#" if x == 1 else "." for x in line]))
    return "lol"


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
