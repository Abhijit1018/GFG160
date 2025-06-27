def longestConsecutive(arr):
    st = set()
    res = 0

    # Hash all the array elements
    for val in arr:
        st.add(val)

    # Check each possible sequence from the start 
    # then update length
    for val in arr:

        # If current element is the starting element of a sequence
        if val in st and (val - 1) not in st:

            # Then check for next elements in the sequence
            cur = val
            cnt = 0
            while cur in st:

                # Remove this number to avoid recomputation
                st.remove(cur)
                cur += 1
                cnt += 1

            # Update optimal length
            res = max(res, cnt)

    return res


if __name__ == "__main__":
    arr = [2, 6, 1, 9, 4, 5, 3]
    print(longestConsecutive(arr))
