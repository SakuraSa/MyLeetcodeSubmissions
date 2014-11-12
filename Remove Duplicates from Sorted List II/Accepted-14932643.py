#Author     : sakura_kyon@hotmail.com
#Question   : Remove Duplicates from Sorted List II
#Link       : https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 376 ms
#Description: 
#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#For example,
#Given `1->2->3->3->4->4->5`, return `1->2->5`.
#Given `1->1->1->2->3`, return `2->3`.
#Show Tags
#Linked List

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

def _count(gen):
    count = {}
    for n in gen:
        count[n.val] = count.get(n.val, 0) + 1
    return count

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
    # @return a ListNode
    def deleteDuplicates(self, head):
        count = _count(_iter(head))
        return _linkup(n for n in _iter(head) if count[n.val] == 1)
        