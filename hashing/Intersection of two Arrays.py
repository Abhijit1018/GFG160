def intersection(a, b):
  
    # Put all elements of a[] in as
    as_set = set(a)

    rs_set = set()
    res = []

    # Traverse through b[]
    for elem in b:
      
        # If the element is in as_set and not yet in rs_set
        if elem in as_set and elem not in rs_set:
            rs_set.add(elem)
            res.append(elem)

    return res

# Driver code
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersection(a, b)
print(" ".join(map(str, res)))
