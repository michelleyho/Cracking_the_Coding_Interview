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

if __name__ == "__main__":
    s1, s2 = "pale", "ple"
    print one_away(s1, s2)
    s1, s2 = "pales", "pale"
    print one_away(s1, s2)
    s1, s2 = "pale", "bale"
    print one_away(s1, s2)
    s1, s2 = "pale", "bae"
    print one_away(s1, s2)
    
