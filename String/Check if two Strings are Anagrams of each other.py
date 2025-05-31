MAX_CHAR = 26

def areAnagrams(s1, s2):
    freq = [0] * MAX_CHAR
    
    # Count frequency of each character in string s1
    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    # Count frequency of each character in string s2
    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False
            
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")
