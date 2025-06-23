def findMin(arr):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
      
        # The current subarray is already sorted, 
        # the minimum is at the low index
        if arr[lo] < arr[hi]:
            return arr[lo]
           
        # We reach here when we have at least
        # two elements and the current subarray
        # is rotated
      
        mid = (lo + hi) // 2

        # The right half is not sorted. So 
        # the minimum element must be in the
        # right half.
        if arr[mid] > arr[hi]:
            lo = mid + 1
          
        # The right half is sorted. Note that in 
        # this case, we do not change high to mid - 1
        # but keep it to mid. As the mid element
        # itself can be the smallest
        else:
            hi = mid

    return arr[lo]

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))
