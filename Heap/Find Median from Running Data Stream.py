# Python program to find Median from Running Data Stream
# Using Heaps

import heapq

# Function to find the median of a stream of data
def getMedian(arr):
    
    # Max heap to store the smaller half of numbers
    leftMaxHeap = []
    
    # Min heap to store the greater half of numbers
    rightMinHeap = []
    
    res = []
  
    for num in arr:
        # Insert new element into max heap (negating for max behavior)
        heapq.heappush(leftMaxHeap, -num)
        
        # Move the top of max heap to min heap to maintain order
        temp = -heapq.heappop(leftMaxHeap)
        heapq.heappush(rightMinHeap, temp)
      
        # Balance heaps if min heap has more elements
        if len(rightMinHeap) > len(leftMaxHeap):
            temp = heapq.heappop(rightMinHeap)
            heapq.heappush(leftMaxHeap, -temp)
        
        # Compute median based on heap sizes
        if len(leftMaxHeap) != len(rightMinHeap):
            median = -leftMaxHeap[0]
        else:
            median = (-leftMaxHeap[0] + rightMinHeap[0]) / 2.0
        
        res.append(median)
    
    return res


if __name__ == "__main__":
    arr = [5, 15, 1, 3, 2, 8]
    res = getMedian(arr)
    
    print(" ".join(f"{median:.2f}" for median in res))
