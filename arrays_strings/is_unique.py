'''
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''
'''
Follow up questions:
- How treat empty string?
'''

'''
Time:O(n) - visit each character once
Space: O(n) - since using hash table
'''
# TODO: no additonal data structures
# TODO: more testcases
def is_unique(word):
    if not word:
        return False

    h = {}
    for c in word:
        h[c] = h.get(c, 0) + 1
        if h[c] > 1:
            return False
    
    return True



if __name__ == "__main__":
    s = "abracadabra"
    print is_unique(s)
    
    s = "xybz"
    print is_unique(s)

    s = "xybzzbyx"
    print is_unique(s)


