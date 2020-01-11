"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.



第一次真正写到滑动窗口的题目
感觉有点难
逻辑没有理清晰
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count  = [0]*26
        L = 0
        R = 0
        max_index = 0
        max_windows = 0
       # index = ord(s[max_count])-ord('A')
        #count[index] = 1
        for R in range(len(s)):
            index = ord(s[R])-ord('A')
            count[index] += 1
            if(count[index] > count[max_index]):
                max_index = index
                
            while(R-L+1-count[max_index]>k):
                count[ord(s[L])-ord('A')] -=1
                L = L+1
                max_index = count.index(max(count))
            if(max_windows < R-L+1):
                max_windows = R-L+1
        return max_wi
