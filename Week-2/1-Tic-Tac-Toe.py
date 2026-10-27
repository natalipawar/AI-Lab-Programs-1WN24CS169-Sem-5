# To implement a Tic-Tac-Toe game in which the computer uses the MINIMAX algorithm to select the best move.



# Tic-Tac-Toe using MINIMAX Algorithm

b = [' '] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def show():
    print("\n    1   2   3")
    for i in range(0, 9, 3):
        print(str(i//3+1) + "   " +
              " | ".join(b[j] if b[j] != ' ' else ' ' for j in range(i, i+3)))
        if i < 6:
            print("   ---+---+---")
    print()

def winner():
    for i, j, k in wins:
        if b[i] == b[j] == b[k] != ' ':
            return b[i]
    return None

def minimax(maximizing):
    w = winner()
    if w == 'O': return 1
    if w == 'X': return -1
    if ' ' not in b: return 0

    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if maximizing else 'X'
            scores.append(minimax(not maximizing))
            b[i] = ' '
    return max(scores) if maximizing else min(scores)

def computer():
    best, move = -2, -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(False)
            b[i] = ' '
            if score > best:
                best, move = score, i
    b[move] = 'O'

print("\n===== TIC-TAC-TOE =====")
print("You are X | Computer is O")
show()

while True:
    try:
        r, c = map(int, input("Your turn (row column): ").split())
        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Invalid position! Enter values from 1 to 3.\n")
            continue
        p = (r-1)*3 + c-1
        if b[p] != ' ':
            print("Position occupied! Try again.\n")
            continue
    except ValueError:
        print("Enter row and column, e.g. 1 1.\n")
        continue

    b[p] = 'X'
    show()

    if winner() == 'X':
        print("Human Player Wins!")
        break
    if ' ' not in b:
        print("Game Draw!")
        break

    print("Computer's turn...")
    computer()
    show()

    if winner() == 'O':
        print("Computer Wins!")
        break
    if ' ' not in b:
        print("Game Draw!")
        break
