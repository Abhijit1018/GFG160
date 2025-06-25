def search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        
        # If x == mid, return true
        if x == arr[mid]:
            return True
        
        # If x < arr[mid], search in the left half
        if x < arr[mid]:
            hi = mid - 1
        
        # If x > arr[mid], search in the right half
        else:
            lo = mid + 1
    return False


def searchRowMatrix(mat, x):
    n, m = len(mat), len(mat[0])
    
    # Iterate over all the rows to find x
    for i in range(n):
        
        # Perform binary search on the ith row
        if search(mat[i], x):
            return True
    
    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [[3, 4, 9],
           [2, 5, 6],
           [9, 25, 27]]
    x = 9
    if searchRowMatrix(mat, x):
        print("true")
    else:
        print("false")
