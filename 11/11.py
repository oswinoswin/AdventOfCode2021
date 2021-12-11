import re
import numpy as np


def first(filename):
    p = re.compile(r'\d')
    octopuses = []
    with open(filename, "r") as f:
        for line in f:
            row = [int(x) for x in p.findall(line)]
            octopuses.append(row)
    octopuses = np.array(octopuses)
    rows, columns = octopuses.shape
    result = 0
    for step in range(100):
        flash = []
        for row in range(rows):
            for column in range(columns):
                octopuses[row, column] += 1
                if octopuses[row, column] > 9:
                    flash.append((row, column))
                    result += 1

        flashed = []
        while flash:
            for row, column in flash:
                start_row = row - 1 if row > 0 else row
                end_row = row + 1 if row < rows - 1 else row
                start_column = column - 1 if column > 0 else column
                end_column = column + 1 if column < columns - 1 else column
                octopuses[start_row:end_row + 1, start_column:end_column + 1] += 1
                flashed.append((row, column))
            for row, column in flash:
                octopuses[row, column] = 0
            flash = []
            rows, columns = octopuses.shape
            for row in range(rows):
                for column in range(columns):
                    if octopuses[row, column] > 9:
                        flash.append((row, column))
                        result += 1
        for row, column in flashed:
            octopuses[row, column] = 0

    return result


def second(filename):
    p = re.compile(r'\d')
    octopuses = []
    with open(filename, "r") as f:
        for line in f:
            row = [int(x) for x in p.findall(line)]
            octopuses.append(row)
    octopuses = np.array(octopuses)
    rows, columns = octopuses.shape
    step = 0
    while True:
        flash = []
        for row in range(rows):
            for column in range(columns):
                octopuses[row, column] += 1
                if octopuses[row, column] > 9:
                    flash.append((row, column))

        flashed = []
        while flash:
            for row, column in flash:
                start_row = row - 1 if row > 0 else row
                end_row = row + 1 if row < rows - 1 else row
                start_column = column - 1 if column > 0 else column
                end_column = column + 1 if column < columns - 1 else column
                octopuses[start_row:end_row + 1, start_column:end_column + 1] += 1
                flashed.append((row, column))
            for row, column in flash:
                octopuses[row, column] = 0
            flash = []
            rows, columns = octopuses.shape
            for row in range(rows):
                for column in range(columns):
                    if octopuses[row, column] > 9:
                        flash.append((row, column))
        for row, column in flashed:
            octopuses[row, column] = 0
        if len(flashed) == 100:
            return step + 1
        step += 1


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
