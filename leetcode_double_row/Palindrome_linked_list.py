"""
Given a singly linked list, determine if it is a palindrome.

Example1:
    Input: 1->2
    Output: false
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(not head):
            return True

        R = head
        L = head
        a = []

        while(R.next):
            a.append(L.val)
            if(not R.next.next):
               R = R.next
            else:
               R = R.next.next
               L = L.next
        L = L.next
        i = len(a)-1
        while(L and i>=0):
            if(L.val == a[i]):
                L = L.next
                i = i-1
            else:
                break
        if(not L and i==-1):
            return True
        else:
            return False

