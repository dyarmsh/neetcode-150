from typing import List

"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another 
string, but the order of the characters can be different.

You should aim for a solution with O(m * n) time and O(m) space, 
where m is the number of strings and n is the length of the longest string.
"""

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Time: O(m*n), where n: length of strs list
    Space: O(m), where m: length of longest string in strs list
    """

    strs_dict = {} # space: O(m) max, if no anagrams

    for string in strs: # O(m)
        lst = [0] * 26
        for char in string: # O(n) max, where n is length(longest string)
            lst[ord(char) - ord('a')] += 1
        
        if strs_dict.get(tuple(lst)): # O(1), if anagram exists
            strs_dict[tuple(lst)].append(string)
        else: # anagram does not exist (yet)
            strs_dict[tuple(lst)] = [string]
    
    return list(strs_dict.values()) # space: O(m) elements


print(groupAnagrams(["act","pots","tops","cat","stop","hat"])) 
# [["hat"],["act", "cat"],["stop", "pots", "tops"]]

print(groupAnagrams(["x"])) 
# [['x']]

print(groupAnagrams([""])) 
# [['']]

