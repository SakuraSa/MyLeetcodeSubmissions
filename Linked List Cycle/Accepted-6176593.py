#Author     : sakura_kyon@hotmail.com
#Question   : Linked List Cycle
#Link       : https://oj.leetcode.com/problems/linked-list-cycle/
#Language   : python
#Status     : Accepted
#Run Time   : 552 ms
#Description: 
#Given a linked list, determine if it has a cycle in it.
#Follow up:
#Can you solve it without using extra space?

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        s = set()
        while not head is None:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False