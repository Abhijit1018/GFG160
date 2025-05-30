def missingNumber(arr):
    n = len(arr)
    for i in range(n):

        # if arr[i] is within the range 1 to n
        # and arr[i] is not placed at (arr[i]-1)th index in arr
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:

            # then swap arr[i] and arr[arr[i]-1] to place arr[i]
            # to its corresponding index
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp

    # If any number is not at its corresponding index, then it
    # is the missing number
    for i in range(1, n + 1):
        if i != arr[i - 1]:
            return i

    # If all number from 1 to n are present 
    # then n + 1 is smallest missing number
    return n + 1


if __name__ == '__main__':
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))
