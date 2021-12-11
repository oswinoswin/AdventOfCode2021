import re


def first(filename):
    p = re.compile(r'\d+')
    fish = []
    with open(filename, "r") as f:
        for line in f:
            fish = [int(i) for i in p.findall(line)]
    return simulate_fish(fish, 80)
    # # print(f"Initial state: {fish}")
    # total_days = 80
    # for day in range(total_days):
    #     for i in range(len(fish)):
    #         if fish[i] > 0:
    #             fish[i] = fish[i] - 1
    #         else:
    #             fish[i] = 6
    #             fish.append(8)
    #     # print(f"After  {day + 1} day: {fish}")
    # return len(fish)


def second(filename):
    p = re.compile(r'\d+')
    fish = []
    with open(filename, "r") as f:
        for line in f:
            fish = [int(i) for i in p.findall(line)]
    return simulate_fish(fish, 256)


def simulate_fish(fish, total_days):
    for day in range(total_days):
        for i in range(len(fish)):
            if fish[i] > 0:
                fish[i] = fish[i] - 1
            else:
                fish[i] = 6
                fish.append(8)
        print(f"Population size after  {day + 1} day: {len(fish)}")
    return len(fish)

if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    # print(second("example.txt"))
    print(second("input.txt"))
