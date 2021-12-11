import re
import numpy as np

def first(filename):
    p = re.compile(r'\d')
    heights = []
    with open(filename, "r") as f:
        for line in f:
            row = [int(x) for x in p.findall(line)]
            heights.append(row)
    heights = np.array(heights)
    risk_sum = 0
    rows, columns = heights.shape
    for row_idx in range(rows):
        for col_idx in range(columns):
            neighbours = []
            current = heights[row_idx, col_idx]
            if row_idx >= 1:
                top = heights[row_idx - 1, col_idx]
                neighbours.append(top)
            if row_idx < rows - 1:
                bottom = heights[row_idx + 1, col_idx]
                neighbours.append(bottom)
            if col_idx >= 1:
                left = heights[row_idx, col_idx - 1]
                neighbours.append(left)
            if col_idx < columns - 1:
                right = heights[row_idx, col_idx + 1]
                neighbours.append(right)
            if current < min(neighbours):
                risk_sum += current + 1
    return risk_sum





def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
