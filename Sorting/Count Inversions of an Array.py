def countAndMerge(arr, l, m, r):
  
    # Counts in two subarrays
    n1 = m - l + 1
    n2 = r - m

    # Set up two lists for left and right halves
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    # Initialize inversion count (or result)
    # and merge two halves
    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:

        # No increment in inversion count
        # if left[] has a smaller or equal element
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1

    # Merge remaining elements
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res

# Function to count inversions in the array
def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2

        # Recursively count inversions
        # in the left and right halves
        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)

        # Count inversions such that greater element is in 
        # the left half and smaller in the right half
        res += countAndMerge(arr, l, m, r)
    return res

def inversionCount(arr):
    return countInv(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))
