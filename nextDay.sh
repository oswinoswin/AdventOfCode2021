#!/bin/bash
mkdir $1
touch $1/$1.py
touch $1/example.txt
touch $1/input.txt

cat > $1/$1.py <<EOL
def first(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
EOL

git add $1