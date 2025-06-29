def sumClosest(arr, target):
    n = len(arr)
    arr.sort()
    res = []
    minDiff = float('inf')

    left = 0
    right = n - 1

    while left < right:
        currSum = arr[left] + arr[right]

        # Check if this pair is closer than the closest
        # pair so far
        if abs(target - currSum) < minDiff:
            minDiff = abs(target - currSum)
            res = [arr[left], arr[right]]

        # If this pair has less sum, move to greater values
        if currSum < target:
            left += 1

        # If this pair has more sum, move to smaller values
        elif currSum > target:
            right -= 1

        # If this pair has sum = target, return it
        else:
            return res

    return res

if __name__ == "__main__":
    arr = [5, 2, 7, 1, 4]
    target = 10

    res = sumClosest(arr, target)
    if len(res) > 0:
    	print(res[0], res[1])
