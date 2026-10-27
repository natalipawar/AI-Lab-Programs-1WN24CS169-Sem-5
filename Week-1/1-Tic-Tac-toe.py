# Implement Tic-Tac-Toe game in general without using any standard algorithm. Game should be played between Human and Computer.


board = [' ' for i in range(9)]

win_positions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i < 6:
            print('--+---+--')
    print()

def check_winner():
    for p in win_positions:
        if board[p[0]] == board[p[1]] == board[p[2]] != ' ':
            return board[p[0]]
    return None

def computer_move():
    # 1. Check if computer can win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner() == 'O':
                return
            board[i] = ' '

    # 2. Block human from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner() == 'X':
                board[i] = 'O'
                return
            board[i] = ' '

    # 3. Choose the first available position
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return

print("TIC-TAC-TOE")
print("You are X and Computer is O")
print("Enter positions from 1 to 9")

display_board()

while True:
    try:
        pos = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos] = 'X'
    display_board()

    if check_winner() == 'X':
        print("Human wins!")
        break

    if ' ' not in board:
        print("It's a draw!")
        break

    computer_move()
    print("Computer played.")
    display_board()

    if check_winner() == 'O':
        print("Computer wins!")
        break

    if ' ' not in board:
        print("It's a draw!")
        break
