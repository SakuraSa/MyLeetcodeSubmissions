#Author     : sakura_kyon@hotmail.com
#Question   : Linked List Cycle II
#Link       : https://oj.leetcode.com/problems/linked-list-cycle-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 604 ms
#Description: 
#Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.
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
    # @return a list node
    def detectCycle(self, head):
        s = set()
        while not head is None:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None