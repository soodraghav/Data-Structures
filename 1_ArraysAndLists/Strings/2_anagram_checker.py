"""
Anagrams:
The goal of this exercise is to write some code to determine if two strings
are anagrams of each other.
An anagram is a word (or phrase) that is formed by rearranging the letters of
another word (or phrase).
For example:
"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
Your function should take two strings as input and return True if the two
words are anagrams and False if they are not.
You can assume the following about the input strings:
No punctuation
No numbers
No special characters
"""


def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other
    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    Time complexity:
        clean_str1: O(n)
        clean_str2: O(m)
        3 for-loops: O(n + m + n) => O(2n + m)
        Total: O(n + m + 2n + m) => O(3n + 2m) => O(n)
    Space complexity:
        str1: O(n)
        str2: O(m)
        clean_str1: O(n)
        clean_Str2: O(m)
        letter_count(dict): O(n)
        Total: O(n + m + n + m + n) => O(3n + 2m) => O(n)
    """

    # TODO: Write your solution here
    str_a =str1.lower().replace(' ','')
    str_b =str2.lower().replace(' ','')
    
    dict = {}
    
    if len(str_a) != len(str_b):
        return False
        
    else:
        for letter in str_a:
            dict[letter] = dict.get(letter,0) + 1
            
        for letter2 in str_b:
            if letter2 in dict:
                dict[letter2] -= 1 
                
            else:
                return False
        
        for key in dict:
            if dict[key] != 0:
                return False
            
   
    return True
            
        
    


def anagram_checker_sort(str1, str2):
    """
    Time complexity:
        clean strings: O(n + n) => O(n)
        sort strings: O(nlogn)
        return string-comparision: O(n) // Added as per Yemissi's advice
        Total: O(n + nlogn + n) => O(nlogn)
    Space complexity:
        str1: O(n)
        str2: O(m)
        clean_str1: O(n)
        clean_str2: O(m)
        Total: O(n + m + n + m) => O(2n+2m) => O(n)
    """

    word1 = sorted(str1.replace(" ",'').lower())
    word2 = sorted(str2.replace(" ",'').lower())
    
    return word1 == word2




# Test Cases
print("Anagram Check with Sort:")
print(anagram_checker_sort('boom', 'moot'))
print(anagram_checker_sort('anagram', 'nag a ram'))
print(anagram_checker_sort('Elegant men', 'Elegant men'))

print("Anagram Check with dictionary:")
print(anagram_checker('boom', 'moot'))
print(anagram_checker('anagram', 'nag a ram'))
print(anagram_checker('Elegant men', 'Elegant men'))