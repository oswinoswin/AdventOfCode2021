def first(filename):
    with open(filename, "r") as f:
        depth = 0
        position = 0
        for line in f:
            l_splitted = line.split()
            command = l_splitted[0]
            value = int(l_splitted[1])
            if command == "forward":
                position += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value
    return depth*position


def second(filename):
    with open(filename, "r") as f:
        depth = 0
        position = 0
        aim = 0
        for line in f:
            l_splitted = line.split()
            command = l_splitted[0]
            value = int(l_splitted[1])
            if command == "forward":
                position += value
                depth += aim * value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value
    return depth*position


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
