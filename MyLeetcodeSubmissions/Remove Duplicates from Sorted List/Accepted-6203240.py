#Author     : sakura_kyon@hotmail.com
#Question   : Remove Duplicates from Sorted List
#Link       : https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
#Language   : python
#Status     : Accepted
#Run Time   : 220 ms
#Description: 
#Given a sorted linked list, delete all duplicates such that each element appear only once.
#For example,
#Given `1->1->2`, return `1->2`.
#Given `1->1->2->3->3`, return `1->2->3`.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head is None:
            s = set()
            s.add(head.val)
            pl = head
            pt = head.next
            while not pt is None:
                if pt.val in s:
                    pt = pt.next
                    pl.next = pt
                    continue
                else:
                    s.add(pt.val)
                pl = pt
                pt = pt.next
                
        return head