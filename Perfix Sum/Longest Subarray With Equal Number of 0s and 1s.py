# Python program to find longest subarray with equal
# number of 0's and 1's Using HashMap and Prefix Sum

def maxLen(arr):
    mp = {}

    preSum = 0
    res = 0

    # Traverse through the given array
    for i in range(len(arr)):

        # Add current element to sum
        # if current element is zero, add -1
        preSum += -1 if arr[i] == 0 else 1

        # To handle sum = 0 at last index
        if preSum == 0:
            res = i + 1

        # If this sum is seen before, then update 
      	# result with maximum
        if preSum in mp:
            res = max(res, i - mp[preSum])

        # Else put this sum in hash table
        else:
            mp[preSum] = i

    return res

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 1]
    print(maxLen(arr))
