# Python program to add two binary strings
# using Bit-by-Bit addition

def trimLeadingZeros(s):
    
    # Find the position of the first '1'
    firstOne = s.find('1')
    return s[firstOne:] if firstOne != -1 else "0"


# This function adds two binary strings and return
# result as a third string
def addBinary(s1, s2):
    
    # Trim Leading Zeros
    s1 = trimLeadingZeros(s1)
    s2 = trimLeadingZeros(s2)
    
    n = len(s1)
    m = len(s2)

    # Swap the strings if s1 is of smaller length
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n

    j = m - 1
    carry = 0
    result = []

    # Traverse both strings from the end
    for i in range(n - 1, -1, -1):

        # Current bit of s1
        bit1 = int(s1[i])
        bitSum = bit1 + carry

        # If there are remaining bits in s2
        # add them to the bitSum
        if j >= 0:
            # Current bit of s2
            bit2 = int(s2[j])
            bitSum += bit2
            j -= 1

        # Calculate the result bit and update carry
        bit = bitSum % 2
        carry = bitSum // 2

        # Update the current bit in result
        result.append(str(bit))

    # If there's any carry left, prepend it to the result
    if carry > 0:
        result.append('1')

    return ''.join(result[::-1])


if __name__ == "__main__":
    s1 = "1101"
    s2 = "111"
    print(addBinary(s1, s2))
