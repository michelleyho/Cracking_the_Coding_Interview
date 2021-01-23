'''
Given two strings, write a method to decide if one is a permutation of the other.
'''
'''
Follow up questions:
 - what if both are empty?  
'''

# TODO: More testcases

'''
Time:O(n) + O(n)
Space:O(n)
'''

def check_permutation(word1, word2):
    if not word1 and not word2:
        return True
    
    h = {}
    for c in word1:
        h[c] = h.get(c, 0) + 1
    
    for c in word2:
        if c in h:
            h[c] -= 1
            if h[c] == 0:
                del h[c]
        else:
            return False

    return False if h else True

if __name__ == "__main__":
    
    s1, s2 = "abde", "edba"
    print check_permutation(s1, s2)

    s1, s2 = "abde", "abdee"
    print check_permutation(s1, s2)
    
    s1, s2 = "abde", ""
    print check_permutation(s1, s2)
    
    s1, s2 = "", ""
    print check_permutation(s1, s2)

    s1, s2 = "", "edba"
    print check_permutation(s1, s2)
