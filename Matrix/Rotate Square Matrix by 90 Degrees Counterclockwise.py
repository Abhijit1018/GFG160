def rotateMatrix(mat):
    n = len(mat)

    # Consider all cycles one by one
    for i in range(n // 2):
        
        # Consider elements in group of 4
        # as P1, P2, P3 & P4 in current square
        for j in range(i, n - i - 1):

            temp = mat[i][j]
            mat[i][j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = temp

# Driver code
if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    rotateMatrix(mat)

    # Print the rotated matrix
    for row in mat:
      print(" ".join(map(str, row)))
