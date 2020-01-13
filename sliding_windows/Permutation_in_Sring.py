"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(len(s1)>len(s2) or len(s2) == 0):
            return False
        a = [0]*26
        sums = 0
        L = 0
        n = len(s1)
        R = n-1
        for s in s1:
            sums +=ord(s)
            index = ord(s)-ord('a')
            a[index] +=1
        sums1 = 0
        for i in range(L,n):
            sums1 += ord(s2[i])

        while(R<len(s2)):
            if sums1 != sums:
                if(R == len(s2)-1):
                    break
                sums1 =  sums1 - ord(s2[L])
                L  = L + 1
                R  = R + 1
                sums1 = sums1 + ord(s2[R])
            else:
                b = [0]*26
                for i in range(L,R+1):
                    index = ord(s2[i])-ord('a')
                    b[index] +=1
                if(a == b):
                    return True
                else:
                    if(R == len(s2)-1):
                        break
                    sums1 =  sums1 - ord(s2[L])
                    L  = L + 1
                    R  = R + 1
                    sums1 = sums1 + ord(s2[R])

        return False

