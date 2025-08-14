# Python program to find the k largest elements in the  
# array using min heap

import heapq

# Function to find the k largest elements in the array 
def kLargest(arr, k):
  
    # Create a min-heap with the first k elements
    minH = arr[:k]
    heapq.heapify(minH)
    
    # Traverse the rest of the array
    for x in arr[k:]:
        if x > minH[0]:
            heapq.heapreplace(minH, x)
    
    res = []

    # Min heap will contain only k 
    # largest element
    while minH:
        res.append(heapq.heappop(minH))

    # Reverse the result array, so that all
    # elements are in decreasing order
    res.reverse()

    return res

if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    res = kLargest(arr, k)
    print(" ".join(map(str, res)))
