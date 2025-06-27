def countSubarrays(arr, k):
    res = 0

    # Pick a starting point of the subarray
    for s in range(len(arr)):
        sum = 0

        # Pick an ending point
        for e in range(s, len(arr)):
            sum += arr[e]
            if sum == k:
                res += 1

    return res

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(countSubarrays(arr, k))
