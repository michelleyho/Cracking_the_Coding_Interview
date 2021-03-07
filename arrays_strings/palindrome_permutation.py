'''
Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome is a word or phrase that is the same forwards or backwards.  A permuration is a rearragement of leters.  The palindrom does not need to be limited to just dictionary words. 
'''

'''
Follow up questions:
 - how deal with spaces in phrase?  Ignore?
    - any other ignorable characters?
 - Case sensitivity? Ignore?
'''
#TODO: more test cases

'''
Time: O(n) + O(n)- go through phrase once, hash once
Space: O(n) - hash needed
'''
def palindrome_permutation(s):
    phrase = s.replace(' ','')
    h = {}

    for char in phrase:
        h[char.lower()] = h.get(char.lower(), 0) + 1

    count = 0
    
    for k, v in h.items():
        count += v%2 
    
    if len(phrase) % 2 == 1:
        return count == 1
    else:
        return count == 0


def test_is_palindrome():
    s = "attccoa"
    assert palindrome_permutation(s)

def test_is_palindrome_with_space():
    s = "tact coa"
    assert palindrome_permutation(s)

def test_is_palindrome_with_mixed_case():
    s = "TactCoa"
    assert palindrome_permutation(s)

def test_not_palindrome():
    s = "attccoad"
    assert not palindrome_permutation(s)

def test_is_plaindromeempty_string():
    s = ""
    assert palindrome_permutation(s)

def test_single_character():
    s = "a"
    assert palindrome_permutation(s)

def test_with_punctuation():
    s = "a;a"
    assert palindrome_permutation(s)


