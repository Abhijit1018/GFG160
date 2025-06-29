def countTriangles(arr):
    res = 0
    arr.sort()

    # Iterate through the array, fixing the largest side at arr[i]
    for i in range(2, len(arr)):
      
        # Initialize pointers for the two smaller sides
        left, right = 0, i - 1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                # arr[left] + arr[right] satisfies the triangle inequality,
                # so all pairs (x, right) with (left <= x < right) are valid
                res += right - left

                # Move the right pointer to check smaller pairs
                right -= 1
                
            else:
                # Move the left pointer to increase the sum
                left += 1

    return res


if __name__ == "__main__":
    arr = [4, 6, 3, 7]
    print(countTriangles(arr))
