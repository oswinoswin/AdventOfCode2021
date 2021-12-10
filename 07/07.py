import re
from statistics import mean
import math


def first(filename):
    p = re.compile(r'\d+')
    crabs = []
    with open(filename, "r") as f:
        for line in f:
            crabs = [int(i) for i in p.findall(line)]
    min_dist = float('inf')

    for crab in crabs:
        dist = calculate_distance_first(crabs, crab)
        print(crab, dist)
        if dist <= min_dist:
            min_dist = dist
    return min_dist




def second(filename):
    p = re.compile(r'\d+')
    crabs = []
    with open(filename, "r") as f:
        for line in f:
            crabs = [int(i) for i in p.findall(line)]
    min_dist = float('inf')
    max_x = max(crabs)
    for centre in range(max_x):
        dist = calculate_distance_second(crabs, centre)
        if dist <= min_dist:
            min_dist = dist
    return min_dist


def calculate_distance_first(x_positions, centre):
    return sum([abs(x - centre) for x in x_positions])


def calculate_distance_second(x_positions, centre):
    total_cost = 0
    for x in x_positions:
        dist = abs(x - centre)
        total_cost += fuel_cost(dist)
    return total_cost

def fuel_cost(distance):
    return ((1 + distance)*distance)/2

if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
