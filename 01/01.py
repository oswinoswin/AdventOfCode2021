def first(filename):
    with open(filename,"r") as f:
        increased_measurements = 0
        prev_depth = None
        for line in f:
            current_depth = int(line)
            if prev_depth is not None and current_depth > prev_depth:
                increased_measurements += 1
            prev_depth = current_depth

    return increased_measurements


def second(filename):
    depths = []
    increased_measurements = 0
    with open(filename, "r") as f:
        for line in f:
            depths.append(int(line))
    prev_sum = sum(depths[:3])
    for i in range(1, len(depths) - 2):
        current_sum = sum(depths[i:i + 3])
        if current_sum > prev_sum:
            increased_measurements += 1
        prev_sum = current_sum
    return increased_measurements


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
