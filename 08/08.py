def first(filename):
    result = 0
    with open(filename, "r") as f:
        for line in f:
            outputs = line.split("|")[1]
            outputs = outputs.strip().split(" ")
            for output in outputs:
                if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
                    print(output)
                    result += 1
    return result



def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
