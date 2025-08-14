# Python program for find k closest point to 
# origin using max heap.
import heapq

# Function to calculate squared
# distance from the origin
def squaredDis(point):
    return point[0] * point[0] + point[1] * point[1]

# Function to find k closest points to the origin
def kClosest(points, k):
    # Max heap to store points with their 
    # squared distances
    maxHeap = []

    # Iterate through each point
    for point in points:
        dist = squaredDis(point)
        
        if len(maxHeap) < k:
          
            # If the heap size is less than k, 
            # insert the point
            heapq.heappush(maxHeap, (-dist, point))
        else:
          
            # If the heap size is k, compare with
            #the top element
            if -dist > maxHeap[0][0]:
              
                # Replace the top element if the current
                #point is closer
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-dist, point))

    # Take the k closest points from the heap
    return [pair[1] for pair in maxHeap]

if __name__ == "__main__":
    points = [[1, 3], [-2, 2], [5, -1], [3, 2], [1, 1]]
    k = 3
    
    res = kClosest(points, k)
    
    # Print the result
    for point in res:
        print('[' + ', '.join(map(str, point)) + ']', end = ' ')
