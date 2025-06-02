def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n
  
    # Length of the previous longest prefix suffix
    patLen = 0

    # lps[0] is always 0
    lps[0] = 0

    # loop calculates lps[i] for i = 1 to n-1
    i = 1
    while i < n:
      
        # If the characters match, increment len 
        # and extend the matching prefix
        if pat[i] == pat[patLen]:
            patLen += 1
            lps[i] = patLen
            i += 1
      
        # If there is a mismatch
        else:
          
            # If len is not zero, update len to
            # last known prefix length
            if patLen != 0:
                patLen = lps[patLen - 1]
            # No prefix matches, set lps[i] = 0
            # and move to the next character
            else:
                lps[i] = 0
                i += 1
    return lps


# Function to check if s1 and s2 are rotations of each other
def areRotations(s1, s2):
    txt = s1 + s1
    pat = s2
    
    # search the pattern string s2 in the concatenation string 
    n = len(txt)
    m = len(pat)

    # Create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = computeLPSArray(pat)
  
    i = 0 
    j = 0
    while i < n:
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == m:
            return True

        # Mismatch after j matches
        elif i < n and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

if __name__ == "__main__":
    s1 = "aab" 
    s2 = "aba"
    
    print("true" if areRotations(s1, s2) else "false")
