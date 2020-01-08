"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):
            return head
        L = head
        R = head
        while(R):
            L = L.next
            if(R.next):
                R = R.next.next
            else:
                R = R.next
                break
            if(L == R):
                L = head
                while(L != R):
                    L = L.next
                    R = R.next
                break
        return R

