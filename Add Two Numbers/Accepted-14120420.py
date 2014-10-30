#Author     : sakura_kyon@hotmail.com
#Question   : Add Two Numbers
#Link       : https://oj.leetcode.com/problems/add-two-numbers/
#Language   : python
#Status     : Accepted
#Run Time   : 816 ms
#Description: 
#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
####Input:### (2 -> 4 -> 3) + (5 -> 6 -> 4)
####Output:### 7 -> 0 -> 8
#Show Tags
#Linked ListMath

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        pt = head = None
        p1, p2 = l1, l2
        add = 0
        while p1 or p2 or add > 0:
            s = add
            if p1:
                s += p1.val
                p1 = p1.next
            if p2:
                s += p2.val
                p2 = p2.next
            p = ListNode(s % 10)
            add = s / 10
            if pt:
                pt.next = p
            pt = p
            if head is None:
                head = pt
        return head
                
                
        