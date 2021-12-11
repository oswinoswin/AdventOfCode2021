from collections import deque

brackets = {"(": ")", "[": "]", "{": "}", "<":">" }


def first(filename):
    points = 0
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    with open(filename, "r") as f:
        for line in f:
            checker = deque()
            chunk = line.strip()
            print(chunk)
            for symbol in chunk:
                if symbol in brackets.keys():
                    checker.append(symbol)
                if symbol in brackets.values():
                    top = checker.pop()
                    print(f"Closing: {symbol} should match with: {top}")
                    if brackets[top] != symbol:
                        points += scores[symbol]
    return points


def second(filename):
    results = []
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    with open(filename, "r") as f:
        for line in f:
            checker = deque()
            chunk = line.strip()
            was_error = False
            for symbol in chunk:
                if symbol in brackets.keys():
                    checker.append(symbol)
                if symbol in brackets.values():
                    top = checker.pop()
                    if brackets[top] != symbol:
                        checker = deque()
                        was_error = True
                        break
            points = 0
            while checker:
                char = checker.pop()
                points = points*5 + scores[char]
            if not was_error:
                results.append(points)
    results.sort()
    return results[len(results)//2]


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
