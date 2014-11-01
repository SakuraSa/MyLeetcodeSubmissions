#Author     : sakura_kyon@hotmail.com
#Question   : Remove Nth Node From End of List
#Link       : https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
#Language   : python
#Status     : Accepted
#Run Time   : 224 ms
#Description: 
#Given a linked list, remove the nth node from the end of list and return its head.
#For example,
#```
#   Given linked list: ###1->2->3->4->5###, and ###n = 2###.
#   After removing the second node from the end, the linked list becomes ###1->2->3->5###.
#```
####Note:###
#Given n will always be valid.
#Try to do this in one pass.
#Show Tags
#Linked ListTwo Pointers

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def link_list_iter(head):
    while head:
        yield head
        head = head.next

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        lst = list(link_list_iter(head))
        if n == len(lst):
            return head.next
        lst[- n - 1].next = lst[-n].next
        return head