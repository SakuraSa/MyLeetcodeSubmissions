#Author     : sakura_kyon@hotmail.com
#Question   : Partition List
#Link       : https://oj.leetcode.com/problems/partition-list/
#Language   : python
#Status     : Accepted
#Run Time   : 180 ms
#Description: 
#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
#For example,
#Given `1->4->3->2->5->2` and x = 3,
#return `1->2->2->4->3->5`.
#Show Tags
#Linked ListTwo Pointers

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def _iter(head):
    while head:
        yield head
        head = head.next

def _join_iter(*args):
    for gen in args:
        for i in gen:
            yield i

def _linkup(gen):
    head = None
    last = None
    for n in gen:
        if head is None:
            head = n
        if last:
            last.next = n
        last = n
    if last:
        last.next = None
    return head

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        less = []
        other = []
        for n in _iter(head):
            if n.val < x:
                less.append(n)
            else:
                other.append(n)
        return _linkup(_join_iter(less, other))
        