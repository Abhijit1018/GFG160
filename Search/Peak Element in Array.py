def peakElement(arr):
    n = len(arr)

    # If there is only one element, then it's a peak
    if n == 1:
        return 0

    # Check if the first element is a peak
    if arr[0] > arr[1]:
        return 0

    # Check if the last element is a peak
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Search Space for binary Search
    lo, hi = 1, n - 2

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # If the element at mid is a  
        # peak element return mid
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        # If next neighbor is greater, then peak
        # element will exist in the right subarray
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1

        # Otherwise, it will exist in left subarray
        else:
            hi = mid - 1


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(peakElement(arr))
