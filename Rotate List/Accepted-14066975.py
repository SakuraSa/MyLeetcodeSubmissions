#Author     : sakura_kyon@hotmail.com
#Question   : Rotate List
#Link       : https://oj.leetcode.com/problems/rotate-list/
#Language   : python
#Status     : Accepted
#Run Time   : 192 ms
#Description: 
#Given a list, rotate the list to the right by k places, where k is non-negative.
#For example:
#Given `1->2->3->4->5->NULL` and k = `2`,
#return `4->5->1->2->3->NULL`.
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
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        lst = list(link_list_iter(head))
        lst[-1].next = lst[0]
        head_index = (-k) % len(lst)
        tail_index = (- k - 1) % len(lst)
        lst[tail_index].next = None
        return lst[head_index]
        