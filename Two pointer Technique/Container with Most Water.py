def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        
        # Find the water stored in the container between 
        # arr[left] and arr[right]
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)
        
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return res

  
if __name__ == "__main__":
	arr = [2, 1, 8, 6, 4, 6, 5, 5]
	print(maxWater(arr))
