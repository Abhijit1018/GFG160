def findUnion(a, b):
    st = set()  
    
    # Put all elements of a[] in st
    for i in range(len(a)):
        st.add(a[i])
    
    # Put all elements of b[] in st
    for i in range(len(b)):
        st.add(b[i])
    
    res = []                            

    # iterate through the set 
    # to fill the result array 
    for it in st:
        res.append(it)
    
    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = findUnion(a, b)

    for i in range(len(res)):
        print(res[i], end = ' ')
