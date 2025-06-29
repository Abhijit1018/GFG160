def longestUniqueSubstr(s):
    n = len(s)
    res = 0

    lastIndex = [-1] * 26

    # Initialize start of current window
    start = 0

    # Move end of current window
    for end in range(n):

        start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)

        # Update result if we get a larger window
        res = max(res, end - start + 1)

        # Update last index of s[end]
        lastIndex[ord(s[end]) - ord('a')] = end

    return res

if __name__ == "__main__":
	s = "geeksforgeeks"
	print(longestUniqueSubstr(s))
