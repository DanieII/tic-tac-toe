from colorama import Fore


def present_game():
    for index, row in enumerate(matrix):
        print(index, *row)
    print("  0 1 2")


def check_for_valid_position(i, j):
    if i in range(3) and j in range(3) and matrix[i][j] == "-":
        return True
    return False


def check_for_identity(lst):
    if lst[0] != "-" and lst[1] != "-" and lst[2] != "-" and lst[0] == lst[1] == lst[2]:
        return True
    return False


def check_for_draw(lst):
    draw = True
    for i in range(3):
        flag = False
        for j in range(3):
            if matrix[i][j] == "-":
                draw = False
                flag = True
                break
            if flag:
                break
    if draw:
        return True
    return False


def check_for_a_winner():
    # Check diagonals
    primary_diagonal = []
    for i in range(len(matrix)):
        sy = matrix[i][i]
        primary_diagonal.append(sy)
    if check_for_identity(primary_diagonal):
        winner = True
    else:
        winner = False
    if winner:
        return True

    second_diagonal = []
    for k in range(len(matrix)):
        sy = matrix[k][-(k + 1)]
        second_diagonal.append(sy)
    if check_for_identity(second_diagonal):
        winner = True
    else:
        winner = False

    if winner:
        return True

    # Check horizontals
    for i in range(len(matrix)):
        current_row = []
        for j in range(len(matrix[i])):
            sy = matrix[i][j]
            current_row.append(sy)
        if check_for_identity(current_row):
            winner = True
            break
        else:
            winner = False

    if winner:
        return True

    # Check verticals
    for col in range(3):
        current_column = []
        # c represents the rows because the loop is between every row with the current column
        for c in range(3):
            current_column.append(matrix[c][col])
        if check_for_identity(current_column):
            winner = True
            break
        else:
            winner = False

    if winner:
        return True
    return False


matrix = [["-" for _ in range(3)] for i in range(3)]
print(Fore.GREEN + "The positions have to be 2 numbers separated by space " + Fore.RESET)
present_game()
print(
    f"Player {Fore.BLUE}1{Fore.RESET} uses {Fore.BLUE}X{Fore.RESET} and player {Fore.RED}2{Fore.RESET} uses {Fore.RED}O{Fore.RESET}")
finished = False
current_player = 1
current_symbol = "X"
while not finished:
    print(f"Now is player {current_player}'s turn")
    while True:
        row, column = [int(x) for x in input("Enter the position ").split()]
        if check_for_valid_position(row, column):
            matrix[row][column] = current_symbol
            present_game()
            break
        else:
            print("The position you entered is either already occupied or invalid. Try again!")
            continue
    if check_for_a_winner():
        print(f"Game Over\nPlayer {current_player} won")
        quit()
    else:
        if check_for_draw(matrix):
            print("Draw\nGame Over")
            quit()

    if current_player == 1:
        current_player = 2
        current_symbol = "O"
    else:
        current_player = 1
        current_symbol = "X"
