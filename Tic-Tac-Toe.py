# Tic-Tac-Toe Game

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def check_draw():
    return " " not in board


def play_game():
    current_player = "X"

    while True:
        print_board()

        try:
            position = int(input(
                f"Player {current_player}, choose a position (1-9): "
            )) - 1

            if position < 0 or position > 8:
                print("Please enter a number from 1 to 9.")
                continue

            if board[position] != " ":
                print("That position is already taken.")
                continue

            board[position] = current_player

            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw():
                print_board()
                print("It's a draw!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")


print("=== TIC-TAC-TOE ===")
print("Positions are numbered like this:")
print()
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

play_game()
