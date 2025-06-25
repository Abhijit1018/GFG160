def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        # Find row and column of element at mid index
        row = mid // m
        col = mid % m

        # If x is found, return true
        if mat[row][col] == x:
            return True

        # If x is greater than mat[row][col], search in
        # right half
        if mat[row][col] < x:
            lo = mid + 1

        # If x is less than mat[row][col], search in
        # left half
        else:
            hi = mid - 1

    return False

if __name__ == "__main__":
    mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
    x = 14

    if searchMatrix(mat, x):
        print("true")
    else:
        print("false")
