'''
Write a method to replace all spaces in a string with "%20".  You may assume that the string has sufficient space at teh end to hold the additional characters, and that you are given the "True" length of the string."
'''

# TODO: more testcases

'''
Time: O(n)
Space: O(n)
    - Python strings are immutable...
      Need to create a new array to modify string
'''
def urlify(phrase, length):
    new_phrase = [None]*len(phrase)
    last_char = phrase[length-1]
    
    right_ptr = len(phrase)-1
    left_ptr = length-1

    while left_ptr >= 0:
        curr = phrase[left_ptr]
        if curr != ' ':
            new_phrase[right_ptr] = curr
            right_ptr -= 1
        else:
            new_phrase[right_ptr-2:right_ptr+1] = '%20' 
            right_ptr -= 3

        left_ptr -= 1
    return ''.join(new_phrase)

def test_urlify():
    p, l = "Mr John Smith    ", 13
    assert urlify(p, l) == "Mr%20John%20Smith"
