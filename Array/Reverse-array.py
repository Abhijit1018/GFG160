# Python Program to reverse an array using temporary array

# function to reverse an array
def reverseArray(arr):
    n = len(arr)
    
    # Temporary array to store elements in reversed order
    temp = [0] * n
  
    # Copy elements from original array to temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]
  
    # Copy elements back to original array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")
