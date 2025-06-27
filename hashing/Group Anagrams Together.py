
MAX_CHAR = 26

# function to generate hash of word s
def getHash(s):
    hashList = []
    freq = [0] * MAX_CHAR
    
    # Count frequency of each character
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    
    # Append the frequency to construct the hash
    for i in range(MAX_CHAR):
        hashList.append(str(freq[i]))
        hashList.append("$")
    
    return ''.join(hashList)

def anagrams(arr):
    res = []
    mp = {}
    
    for i in range(len(arr)):
        key = getHash(arr[i])
        
        # If key is not present in the hash map, add
        # an empty group (list) in the result and
        # store the index of the group in hash map
        if key not in mp:
            mp[key] = len(res)
            res.append([])
        
        # Insert the string in its correct group
        res[mp[key]].append(arr[i])
    
    return res

if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    
    res = anagrams(arr)
    for group in res:
        for word in group:
            print(word, end=" ")
        print()
