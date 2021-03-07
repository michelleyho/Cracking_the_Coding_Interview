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

def test_is_permutation():
    s1, s2 = "abde", "edba"
    assert check_permutation(s1, s2) == True

def test_not_permutation():
    s1, s2 = "abde", "abdee"
    assert check_permutation(s1, s2) == False

def test_str1_empty():
    s1, s2 = "", "edba"
    assert check_permutation(s1, s2) == False
def test_str2_empty():
    s1, s2 = "abde", ""
    assert check_permutation(s1, s2) == False
def test_both_empty():
    s1, s2 = "", ""
    assert check_permutation(s1, s2) == True
