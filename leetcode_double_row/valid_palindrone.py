### 解题思路
此处撰写解题思路
1.注意最后一行的翻转a[::-1]
2.filter函数的高级用法
### 代码

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[*filter(str.isalnum,s.lower())]
        return s == s[::-1]
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n= len(s)
        if(n==0):
            return True
        a =[]
        boolen = True
        for i in s.lower():
            if('a'<= i<='z' or '0'<= i <= '9'):
                a.append(i)
        L = 0
        R = len(a)-1
        while(L<R):
            if(a[L] == a[R]):
                L =L + 1
                R =R - 1
            else:
                boolen = False
                break
        return boolen
'''
