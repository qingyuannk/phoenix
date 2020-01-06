### 解题思路
此处撰写解题思路
1.注意最后一行的翻转a[::-1]
2.filter函数的高级用法
### 代码

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[*filter(str.isalnum,s.lower())]
        return s == s[::-1]
