#C++ program to print unique permutation of string 
#using hash map.

# Recursive function to generate permutations
def genPermutations(n, curr, cnt, res):
  
    # Base case: If the current permutation length equals 
    # the input string length, add it to the result
    if len(curr) == n:
        res.append(curr)
        return

    # Iterate through each character in the frequency map
    for c, count in cnt.items():
        # Skip characters with a count of 0
        if count == 0:
            continue

        # Include the character in the current permutation
        cnt[c] -= 1

        # Recur to build the next character in the permutation
        genPermutations(n, curr + c, cnt, res)

        # Backtrack: Restore the count
        cnt[c] += 1

# Function to find all unique permutations of the input string
def findPermutation(s):
  
     # List to store the result
    res = []
    
     # Frequency map to count occurrences of each character
    cnt = {} 

    # Populate the frequency map with the characters of the input string
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1

    # Generate permutations
    genPermutations(len(s), "", cnt, res)
    return res

if __name__ == "__main__":
    s = "ABC"
    res = findPermutation(s)

    print(" ".join(res))
