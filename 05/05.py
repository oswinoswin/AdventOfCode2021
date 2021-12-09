import re
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point(x: {self.x}, y: {self.y})"


def first(filename):
    p = re.compile(r'\d+')
    lines = []
    max_x, max_y = 0, 0
    with open(filename, "r") as f:
        for line in f:
            x1, y1, x2, y2 = [int(i) for i in p.findall(line)]
            max_x = max(x1, x2, max_x)
            max_y = max(y1, y2, max_y)
            lines.append((Point(x1, y1), Point(x2, y2)))
    points = np.zeros((max_y + 1, max_x + 1))

    for line in lines:
        p1, p2 = line
        if p1.x == p2.x:
            for row in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                points[row, p1.x] += 1
        elif p1.y == p2.y:
            for column in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                points[p1.y, column] += 1
    # print(points)
    result = 0
    for point in points.flatten():
        if point >= 2:
            result +=1
    return result



def second(filename):
    p = re.compile(r'\d+')
    lines = []
    max_x, max_y = 0, 0
    with open(filename, "r") as f:
        for line in f:
            x1, y1, x2, y2 = [int(i) for i in p.findall(line)]
            max_x = max(x1, x2, max_x)
            max_y = max(y1, y2, max_y)
            lines.append((Point(x1, y1), Point(x2, y2)))
    points = np.zeros((max_y + 1, max_x + 1))

    for line in lines:
        p1, p2 = line
        if p1.x == p2.x:
            for row in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                points[row, p1.x] += 1
            continue
        elif p1.y == p2.y:
            for column in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                points[p1.y, column] += 1
            continue

        slope = (p2.x - p1.x)/(p2.y - p1.y)
        if slope == 1:
            start_x = min(p1.x, p2.x)
            stop_x = max(p1.x, p2.x)
            start_y = min(p1.y, p2.y)
            dist = stop_x - start_x
            for step in range(dist + 1):
                points[start_y + step, start_x + step] += 1
        if slope == -1:
            start_x = min(p1.x, p2.x)
            stop_x = max(p1.x, p2.x)
            start_y = min(p1.y, p2.y)
            stop_y = max(p1.y, p2.y)
            dist = stop_x - start_x
            for step in range(dist + 1):
                points[stop_y - step, start_x + step] += 1

    result = 0
    for point in points.flatten():
        if point >= 2:
            result +=1
    return result


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
