def Help():
    print("Game rules:")
    print("- This is a 2-player Tic Tac Toe game.")
    print("- The board has positions 1 to 9.")
    print("- Players take turns entering a number to place X or O.")
    print("- First to get 3 in a row (row, column, or diagonal) wins.")
    print("- If all spots are filled and no one wins, it is a draw.\n")


def printBoard(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")


def editBoard(board, inp, symbol):

    idx = inp - 1

    if idx < 0 or idx > 8:
        print("Invalid position! Choose 1-9.")
        return False

    if board[idx] == "X" or board[idx] == "O":
        print("That position is already taken!")
        return False
    board[idx] = symbol
    return True


def checkWin(board):
    win_patterns = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c]:
            return True
    return False


def isDraw(board):
    return all(str(x) in ["X", "O"] for x in board)


if __name__ == "__main__":
    print("welcome to Tic Tac Toe")
    while True:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("\nMain Menu:")
        print("1. Play a Board")
        print("2. Help on game")
        print("3. Quit")
        try:
            choice = int(input("Enter your choice (1,2,3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            printBoard(board)
            turn = 0
            while True:
                if turn == 0:
                    symbol = "X"
                    try:
                        inp = int(input("Player X turn, enter number to place X: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                else:
                    symbol = "O"
                    try:
                        inp = int(input("Player O turn, enter number to place O: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                if not editBoard(board, inp, symbol):
                    continue

                printBoard(board)

                if checkWin(board):
                    print(f"Player {symbol} wins!")
                    break

                if isDraw(board):
                    print("It's a draw!")
                    break

                turn = 1 - turn

        elif choice == 2:
            Help()
            continue
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter 1, 2, or 3.")
            continue
