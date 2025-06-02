def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n

    # lps[0] is always 0
    len_lps = 0

    # loop calculates lps[i] for i = 1 to n-1
    i = 1
    while i < n:
      
        # If the characters match, increment len
        # and set lps[i]
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        
        # If there is a mismatch
        else:
          
            # If len is not zero, update len to 
            # the last known prefix length
            if len_lps != 0:
                len_lps = lps[len_lps - 1]
                
			# No prefix matches, set lps[i] to 0
            else:
                lps[i] = 0
                i += 1
    return lps

# Method returns minimum character to be added at
# front to make string palindrome
def minChar(s):
    n = len(s)
    rev = s[::-1]

    # Get concatenation of string, special character
    # and reverse string
    s = s + "$" + rev

    # Get LPS array of this concatenated string
    lps = computeLPSArray(s)

    # By subtracting last entry of lps array from
    # string length, we will get our result
    return n - lps[-1]

if __name__ == "__main__":
    s = "AACECAAAA"
    print(minChar(s))
