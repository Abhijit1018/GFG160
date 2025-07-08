def check(arr, k, pageLimit):
    
    # Starting from the first student
    cnt = 1
    pageSum = 0
    for pages in arr:
        
        # If adding the current book exceeds the page 
        # limit, assign the book to the next student
        if pageSum + pages > pageLimit:
            cnt += 1
            pageSum = pages
        else:
            pageSum += pages
            
    # If books can assigned to less than k students then
    # it can be assigned to exactly k students as well
    return cnt <= k

def findPages(arr, k):
    
  
    if k > len(arr):
        return -1
    
    # Search space for Binary Search
    lo = max(arr)
    hi = sum(arr)
    res = -1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if check(arr, k, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
            
    return res

if __name__ == "__main__":
    arr = [12, 34, 67, 90]
    k = 2
    print(findPages(arr, k))
