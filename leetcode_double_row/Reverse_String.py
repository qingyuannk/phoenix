"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
Example:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if(len(s)<2):
            return
        L = 0
        R = len(s)-1

        while(L<R):
            s[L] = chr((ord(s[L])^ord(s[R])))
            s[R] = chr(ord(s[R])^ord(s[L]))
            s[L] = chr(ord(s[L])^ord(s[R]))
            L =L+1
            R = R-1

