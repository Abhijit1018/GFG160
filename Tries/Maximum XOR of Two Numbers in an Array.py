# Function to find the maximum XOR
def maxXor(arr):
    res = 0
    mask = 0

    # to store all unique bits
    s = set()

    for i in range(30, -1, -1):

        # set the i-th bit in mask
        mask |= (1 << i)

        for num in arr:

            # keep prefix of all elements
            # till the i-th bit
            s.add(num & mask)

        cur = res | (1 << i)

        for prefix in s:
            if cur ^ prefix in s:
                res = cur
                break

        s.clear()

    return res


if __name__ == "__main__":
    arr = [26, 100, 25, 13, 4, 14]
    print(maxXor(arr))
