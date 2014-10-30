#Author     : sakura_kyon@hotmail.com
#Question   : Add Two Numbers
#Link       : https://oj.leetcode.com/problems/add-two-numbers/
#Language   : python
#Status     : Accepted
#Run Time   : 712 ms
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

def link_add(*args):
    nodes = [node for node in args if node]
    pt = head = None
    add = 0
    while any(nodes) or add > 0:
        s = add
        next_nodes = []
        for node in nodes:
            s += node.val
            if node.next:
                next_nodes.append(node.next)
        nodes = next_nodes
        p = ListNode(s % 10)
        add = s / 10
        if pt:
            pt.next = p
        pt = p
        if head is None:
            head = pt
    return head
                

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return link_add(l1, l2)
                
                
        