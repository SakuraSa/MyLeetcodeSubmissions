#Author     : sakura_kyon@hotmail.com
#Question   : Reverse Linked List II
#Link       : https://oj.leetcode.com/problems/reverse-linked-list-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 156 ms
#Description: 
#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#For example:
#Given `1->2->3->4->5->NULL`, m = 2 and n = 4,
#return `1->4->3->2->5->NULL`.
####Note:###
#Given m, n satisfy the following condition:
#1 ≤ m ≤ n ≤ length of list.
#Show Tags
#Linked List

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def iter_link_list(head):
    while head:
        yield head
        head = head.next

def link_node_as_iter_order(iterable):
    head = None
    last = None
    for node in iterable:
        if head is None:
            head = node
        if last:
            last.next = node
        last = node
    last.next = None
    return head
    

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        lst = list(iter_link_list(head))
        for i, j in zip(range(m - 1, n), reversed(range(m - 1, n))):
            if i > j:
                break
            lst[i], lst[j] = lst[j], lst[i]
        return link_node_as_iter_order(lst)
        