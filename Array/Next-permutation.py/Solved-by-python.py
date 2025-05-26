# Python Program to find the next permutation by 
# generating only next

def next_permutation(arr):
    n = len(arr)
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


arr = [ 2, 4, 1, 7, 5, 0 ]
next_permutation(arr)
print(" ".join(map(str, arr)))
