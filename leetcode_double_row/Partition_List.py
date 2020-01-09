"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x
Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(not head):
            return head
        L = head
        while(L and L.val>=x):
            if(L.next and L.next.val<x):
                print(1)
                N = L.next
                L.next = L.next.next
                N.next = head
                head = N
                L  = N
                break
            L = L.next

        R = head
        while(R):
            if(R.val>= x):
                break
            R = R.next

        if(not L or not R):
            return head

        M = head.next
        while(M):
            if(M.val < x):
                if(L.next == M):
                    L = L.next
                else:
                    N = M
                    M = M.next
                    R.next = M
                    N.next = L.next
                    L.next = N
                    L = L.next
                    continue
            else:
                if(R.next == M):
                    R = R.next
            M = M.next

        return
    """
    判断条件失误
    思考不深入

    """
