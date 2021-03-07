'''
There are three types of edits that can be performed on strings: isnert a character, remove a character, or replace a character.  Given two strings, write a function to check if they are one edit (or zero edits) away."
'''

'''
Follow up questions:
- 
'''

'''
Time: O(n)
Space:O(1)
'''

# TODO: more test cases
# Method #2?

def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):
        return one_away(s2, s1)
    
    diff_count = 0
    ptr1, ptr2 = 0, 0
    while ptr1 < len(s1) and ptr2 < len(s2):
        if s1[ptr1] != s2[ptr2]:
            diff_count += 1
            if diff_count > 1:
                return False
            if len(s1) == len(s2):
                ptr1 += 1
        else:
            ptr1 += 1
        
        ptr2 += 1

    return True 

def test_delete_one():
    s1, s2 = "pale", "ple"
    assert one_away(s1, s2) == True

def test_add_one():
    s1, s2 = "pales", "pale"
    assert one_away(s1, s2) == True

def test_edit_one():
    s1, s2 = "pale", "bale"
    assert one_away(s1, s2) == True

def test_two_edits():
    s1, s2 = "pale", "bae"
    assert one_away(s1, s2) == False

def test_add_two():
    s1, s2 = "pala", "palace"
    assert not one_away(s1, s2)
def test_no_edits():
    s1, s2 = "pale", "pale"
    assert one_away(s1, s2) == True
