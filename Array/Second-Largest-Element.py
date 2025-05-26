class Solution:
    def getSecondLargest(self,arr):
        n = len(arr)
        
        largest = -1
        secondlargest = -1
        
        for i in range(n):
            if arr[i]>largest:
                secondlargest = largest
                largest = arr[i]
                
            elif arr[i]<largest and arr[i]>secondlargest:
                secondlargest = arr[i]
                
        return secondlargest
    
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
            
