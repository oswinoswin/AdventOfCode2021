def first(filename):
    with open(filename, "r") as f:
        line_counter = 0
        gamma = None
        for line in f:
            if gamma == None:
                gamma = [0 for _ in range(len(line) - 1)]
            for i in range(len(gamma)):
                gamma[i] += int(line[i])

            line_counter += 1
        print(gamma)

        epsilon = ["0" for _ in gamma]
        for i in range(len(gamma)):
            if gamma[i] > line_counter - gamma[i]:
                gamma[i] = "1"
                epsilon[i] = "0"
            else:
                gamma[i] = "0"
                epsilon[i] = "1"
        gamma_value_str = "".join([x for x in gamma])
        epsilon_value_str = "".join([x for x in epsilon])
        print(gamma_value_str)
        gamma_value = int(gamma_value_str, 2)
        epsilon_value = int(epsilon_value_str, 2)
        print(epsilon_value_str)
        return gamma_value * epsilon_value




def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))
