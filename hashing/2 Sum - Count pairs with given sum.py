def countPairs(arr, target):
    freq = {}
    cnt = 0

    for i in range(len(arr)):
        
        # Check if the complement (target - arr[i])
        # exists in the map. If yes, increment count
        if (target - arr[i]) in freq:
            cnt += freq[target - arr[i]] 
        
        # Increment the frequency of arr[i]
        freq[arr[i]] = freq.get(arr[i], 0) + 1 
    return cnt

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5] 
    target = 6 
    print(countPairs(arr, target))
