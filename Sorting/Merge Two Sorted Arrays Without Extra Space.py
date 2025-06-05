def mergeArrays(a, b):
  
    # Traverse b[] starting from the last element
    for i in range(len(b) - 1, -1, -1):
      
        # If b[i] is smaller than the largest element of a[]
        if a[-1] > b[i]:
          
            # Place b[i] in the correct position in a[], 
            # and move last element of a[] to b[]
            last = a[-1]
            j = len(a) - 2
            while j >= 0 and a[j] > b[i]:
                a[j + 1] = a[j]
                j -= 1
            
            a[j + 1] = b[i]
            b[i] = last

if __name__ == "__main__":
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    mergeArrays(a, b)

    for ele in a:
        print(ele, end=" ")
    print();
    for ele in b:
        print(ele, end=" ")
