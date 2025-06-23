def kthMissing(arr, k):
    lo = 0
    hi = len(arr) - 1
    res = len(arr) + k

    # Binary Search for index where arr[i] > (i + k)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > mid + k:
            res = mid + k
            hi = mid - 1
        else:
            lo = mid + 1

    return res

if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthMissing(arr, k))
