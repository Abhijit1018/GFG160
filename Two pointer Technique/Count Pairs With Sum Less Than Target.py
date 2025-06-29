def countPairs(arr, target):
  
    # Sort the array to use two pointer technique
    arr.sort()
    left, right = 0, len(arr) - 1
    cnt = 0

    # Two pointer technique
    while left < right:
        sum = arr[left] + arr[right]

        # If the sum is less than target, then arr[left] 
        # will form a valid pair with every element 
        # from index left + 1 to right.
        if sum < target:
            cnt += right - left
            left += 1
        else:
            right -= 1

    return cnt

if __name__ == "__main__":
    arr = [2, 1, 8, 3, 4, 7, 6, 5]
    target = 7
    print(countPairs(arr, target))
