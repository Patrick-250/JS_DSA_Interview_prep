"""given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def valid_anagram(s:str,t:str):
    if len(s) != len(t):
        return False
    dict={}
    for char in s:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    for char in t:
        if char not in dict:
            return False
        dict[char]-=1
        if dict[char]<0:
            return False
    return True

print(valid_anagram( "anagram","nagaram"))