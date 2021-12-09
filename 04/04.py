import numpy as np
import re


def first(filename):
    numbers, boards = read_input(filename)
    selected = np.zeros(boards.shape)

    boards_num, rows, columns = boards.shape
    print(boards[0,:, 2])
    for number in numbers:
        mark_number(number, boards, selected)

        for board_index in range(boards_num):
            selected_board = selected[board_index]
            print(selected_board)
            for row in range(rows):
                if selected_board[row].sum() == rows:
                    print(selected_board)
                    return number*sum_of_unselected(boards[board_index], selected_board)
            for col in range(columns):
                if selected_board[:,col].sum() == columns:
                    return number*sum_of_unselected(boards[board_index], selected_board)


def second(filename): #find last to win
    numbers, boards = read_input(filename)
    selected = np.zeros(boards.shape)

    boards_num, rows, columns = boards.shape
    last_winning_board = None
    last_winning_number = None
    winning_boards = []
    for idx, number in enumerate(numbers):
        mark_number(number, boards, selected)

        for board_index in range(boards_num):
            if board_index in winning_boards:
                continue
            selected_board = selected[board_index]
            is_winning = False
            for row in range(rows):
                if selected_board[row].sum() == rows:
                    is_winning = True
            for col in range(columns):
                if selected_board[:, col].sum() == columns:
                    is_winning = True

            if is_winning:
                last_winning_board = board_index
                winning_boards.append(board_index)
            if len(winning_boards) == boards_num:
                return number * sum_of_unselected(boards[last_winning_board], selected_board)



def read_input(filename):
    with open(filename, "r") as f:
        first_line = f.readline()
        numbers = [int(x) for x in first_line.split(",")]
        boards = []
        f.readline() #skip empty line
        line = f.readline()

        board = []
        while line:
            if len(line) > 1:
                temp = re.findall(r'\d+', line)
                res = list(map(int, temp))
                board.append(res)
            else:
                boards.append(board)
                board = []
            line = f.readline()

        boards.append(board)
        boards = np.array(boards)
        return numbers, boards


def check_board_for_bingo(selected):
    rows, columns = selected.shape
    for row in range(rows):
        if selected[row].sum() == rows:
            return True
    for column in range(columns):
        if selected[:, column].sum() == columns:
            return True
    return False


def mark_number(number, boards, selected):
    boards_num, rows, columns = boards.shape
    for board_index in range(boards_num):
        for row in range(rows):
            for col in range(columns):
                if boards[board_index, row, col] == number:
                    selected[board_index, row, col] = 1


def sum_of_unselected(board, selected):
    rows, columns = selected.shape
    result = 0
    for row in range(rows):
        for col in range(columns):
            if selected[row, col] == 0:
                result += board[row, col]
    return result


if __name__ == "__main__":
    # print(first("example.txt"))
    # print(first("input.txt"))
    print(second("example.txt"))
    print(second("input.txt"))
