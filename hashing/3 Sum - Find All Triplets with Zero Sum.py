def findTriplets(arr):
    
    # Map to store indices for each value
    map = {}

    # Resultant array
    ans = []
    
    # Check for all pairs i, j
    for j in range(len(arr)):
        for k in range(j + 1, len(arr)):
            
            # Value of third index should be 
            val = -1 * (arr[j] + arr[k])
            
            # If such indices exist
            if val in map:
                
                # Append the i, j, k
                for i in map[val]:
                    ans.append([i, j, k])
        
        # After j'th index is traversed
        # We can use it as i.
        if arr[j] not in map:
            map[arr[j]] = []
        map[arr[j]].append(j)
    
    return ans

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    res = findTriplets(arr)
    for triplet in res:
        print(triplet[0], triplet[1], triplet[2])
