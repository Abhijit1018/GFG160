# Function to calculate the product of all elements 
# except the current element

def productExceptSelf(arr):
    zeros = 0
    idx = -1
    prod = 1

    # Count zeros and track the index of the zero
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= arr[i]

    res = [0] * len(arr)

    # If no zeros, calculate the product for all elements
    if zeros == 0:
        for i in range(len(arr)):
            res[i] = prod // arr[i]
    # If one zero, set product only at the zero's index
    elif zeros == 1:
        res[idx] = prod

    return res


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(" ".join(map(str, res)))
