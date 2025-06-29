def countPairs(arr, target):
    res = 0
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:

        # If sum is greater
        if arr[left] + arr[right] < target:
            left += 1

        # If sum is lesser
        elif arr[left] + arr[right] > target:
            right -= 1

        # If sum is equal
        else:
            cnt1 = 0
            cnt2 = 0
            ele1 = arr[left]
            ele2 = arr[right]

            # Count frequency of first element of the pair
            while left <= right and arr[left] == ele1:
                left += 1
                cnt1 += 1

            # Count frequency of second element of the pair
            while left <= right and arr[right] == ele2:
                right -= 1
                cnt2 += 1

            # If both the elements are same, then count of
            # pairs = the number of ways to choose 2
            # elements among cnt1 elements
            if ele1 == ele2:
                res += (cnt1 * (cnt1 - 1)) // 2

            # If the elements are different, then count of
            # pairs = product of the count of both elements
            else:
                res += (cnt1 * cnt2)

    return res


if __name__ == "__main__":
    arr = [-1, 1, 5, 5, 7]
    target = 6

    print(countPairs(arr, target))
