def countTriplets(arr, target):
    n = len(arr)
    res = 0

    # Iterate through each element as the first element of the triplet
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        # Use two-pointer approach to find triplets
        while left < right:

            # Calculate the sum of the triplet
            sum = arr[i] + arr[left] + arr[right]

            # If sum is smaller, move to bigger values
            if sum < target:
                left += 1

            # If sum is greater, move to smaller values
            elif sum > target:
                right -= 1

            # If sum is equal to target
            else:
                ele1 = arr[left]
                ele2 = arr[right]
                cnt1 = 0
                cnt2 = 0

                # Count frequency of the current value at 'left'
                while left <= right and arr[left] == ele1:
                    left += 1
                    cnt1 += 1

                # Count frequency of the current value at 'right'
                while left <= right and arr[right] == ele2:
                    right -= 1
                    cnt2 += 1

                # If both the elements are the same, then count of pairs 
                # = the number of ways to choose 2 elements among cnt1 elements
                if ele1 == ele2:
                    res += (cnt1 * (cnt1 - 1)) // 2

                # If the elements are different, then count of pairs 
                # = product of the count of both elements
                else:
                    res += (cnt1 * cnt2)

    return res


if __name__ == "__main__":
    arr = [-3, -1, -1, 0, 1, 2]
    target = -2
    print(countTriplets(arr, target))
