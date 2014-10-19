#Author     : sakura_kyon@hotmail.com
#Question   : Merge Two Sorted Lists
#Link       : https://oj.leetcode.com/problems/merge-two-sorted-lists/
#Language   : python
#Status     : Accepted
#Run Time   : 212 ms
#Description: 
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        p1, p2 = l1, l2
        head = None
        if p1 is None:
            head = ListNode(p2.val)
            p2 = p2.next
        elif p2 is None:
            head = ListNode(p1.val)
            p1 = p1.next
        elif p1.val < p2.val:
            head = ListNode(p1.val)
            p1 = p1.next
        else:
            head = ListNode(p2.val)
            p2 = p2.next
        ph = head
        while not(p1 is None and p2 is None):
            if p1 is None:
                ph.next = ListNode(p2.val)
                ph = ph.next
                p2 = p2.next
            elif p2 is None:
                ph.next = ListNode(p1.val)
                ph = ph.next
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    ph.next = ListNode(p1.val)
                    ph = ph.next
                    p1 = p1.next  
                else:
                    ph.next = ListNode(p2.val)
                    ph = ph.next
                    p2 = p2.next
        return head
        
        