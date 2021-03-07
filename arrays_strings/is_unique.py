import pytest
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

def test_not_unique():
    words = ["abracadrabra", "xybzzbyx"]
    for word in words:
        assert is_unique(word) == False

def test_unique():
    word = "xybz"
    assert is_unique(word) == True

def test_single_letter():
    word = "a"
    assert is_unique(word) == True
def test_empty_string():
    word = ""
    assert is_unique(word) == False


