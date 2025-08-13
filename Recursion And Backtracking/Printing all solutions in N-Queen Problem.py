# Python program to find all solutions of the N-Queens problem
# using backtracking and pruning

def nQueenUtil(j, n, board, rows, diag1, diag2, res):

    if j > n:
        # A solution is found
        res.append(board[:])
        return

    for i in range(1, n + 1):
        if not rows[i] and not diag1[i + j] and not diag2[i - j + n]:

            # Place queen
            rows[i] = diag1[i + j] = diag2[i - j + n] = True
            board.append(i)

            # Recurse to the next column
            nQueenUtil(j + 1, n, board, rows, diag1, diag2, res)

            # Remove queen (backtrack)
            board.pop()
            rows[i] = diag1[i + j] = diag2[i - j + n] = False

def nQueen(n):
    res = []
    board = []

    # Rows occupied
    rows = [False] * (n + 1)

    # Major diagonals (row + j) and Minor diagonals (row - col + n)
    diag1 = [False] * (2 * n + 1)
    diag2 = [False] * (2 * n + 1)

    # Start solving from the first column
    nQueenUtil(1, n, board, rows, diag1, diag2, res)
    return res

if __name__ == "__main__":
    n = 4
    res = nQueen(n)

    for temp in res:
        print(temp)
