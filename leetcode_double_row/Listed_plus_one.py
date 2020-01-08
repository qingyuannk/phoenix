"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
"""
solution one 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int,list(str(int("".join(map(str,digits)))+1))))
    
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return []
        else:
            n = len(digits)
            while(n>0):
                if(digits[n-1] == 9):
                    digits[n-1] = 0
                    n= n-1
                else:
                    digits[n-1] = digits[n-1]+1
                    break
                if(n==0):
                    digits[0] =1
                    digits.append(0)


        return digits
