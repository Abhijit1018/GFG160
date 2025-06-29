def subarraySum(arr, target):
    # Initialize window
    s, e = 0, 0
    res = []

    curr = 0
    for i in range(len(arr)):
        curr += arr[i]

        # If current sum becomes more or equal,
        # set end and try adjusting start
        if curr >= target:
            e = i

            # While current sum is greater, 
            # remove starting elements of current window
            while curr > target and s < e:
                curr -= arr[s]
                s += 1

            # If we found a subarray
            if curr == target:
                res.append(s + 1)
                res.append(e + 1)
                return res

    # If no subarray is found
    return [-1]
  	
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = subarraySum(arr, target)

    print(" ".join(map(str, res)))
