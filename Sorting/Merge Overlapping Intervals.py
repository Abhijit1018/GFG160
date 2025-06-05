def mergeOverlap(arr):
    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])
