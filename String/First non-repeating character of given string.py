def nonRep(s):
    MAX_CHAR = 26
    vis = [-1] * MAX_CHAR

    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if vis[index] == -1:
            
            # Store the index when character is first seen
            vis[index] = i  
        else:
            
            # Mark character as repeated
            vis[index] = -2  

    idx = -1

    # Find the smallest index of the non-repeating characters
    for i in range(MAX_CHAR):
        if vis[i] >= 0 and (idx == -1 or vis[i] < vis[idx]):
            idx = i

    return '$' if idx == -1 else s[vis[idx]]


s = "aabbccc"
print(nonRep(s))
