"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    board = []
    for i in range(1, 10):
        board.append(i)
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    return type(board[position]) != str


def fill_spot(board, position, character):
    board[position] = character


def winning_game(board):
    combos = ["1,2,3", "4,5,6", "7,8,9", "1,4,7", "2,5,6", "3,6,9", "1,5,9", "7,5,3"]
    for i in range(len(combos)):
        line = combos[i].split(",")
        for j in range(3):
            line[j] = eval(line[j]) - 1
        if board[line[0]] == "X" and board[line[1]] == "X" and board[line[2]] == "X":
            return True
        elif board[line[0]] == "O" and board[line[1]] == "O" and board[line[2]] == "O":
            return True
    return False


def game_over(board):
    count = 0
    for i in range(9):  # Checks if each position is filled
        if type(board[i]) == int:   # if a position in the board list is an int, it has not been chosen and thus the game continues
            count += 1
    if count > 0:
        return winning_game(board)
    else:
        return True


def get_winner(board):
    x_count = 0
    o_count = 0
    for i in range(9):
        if board[i] == "X":
            x_count += 1
        elif board[i] == "O":
            o_count += 1
    total = x_count + o_count
    if (x_count > o_count) and (total < 9):
        return "X"
    elif x_count == o_count:
        return "O"
    else:
        return


def play(board):
    game_end = False
    count = 0
    while not game_end:
        if count % 2 == 0:
            print_board(board)
            pos = eval(input("X's turn to choose a position: ")) - 1
            if is_legal(board, pos):
                count += 1
                fill_spot(board, pos, "X")
                if game_over(board):
                    print_board(board)
                    winner = get_winner(board)
                    if type(winner) == str:
                        print("the winner is ", winner)
                        game_end = True
                    else:
                        print("there is a tie")
                        game_end = True
        else:
            print_board(board)
            pos = eval(input("O's turn to choose a position: ")) - 1
            if is_legal(board, pos):
                count += 1
                fill_spot(board, pos, "O")
                if game_over(board):
                    print_board(board)
                    winner = get_winner(board)
                    if type(winner) == str:
                        print("the winner is ", winner)
                        game_end = True
                    else:
                        print("there is a tie")
                        game_end  = True


def main():
    done = False
    while not done:
        pboard = build_board()
        play(pboard)
        again = input("would you like to play again? (enter yes or no) ")
        if again == "no":
            done = True


if __name__ == '__main__':
    main()
