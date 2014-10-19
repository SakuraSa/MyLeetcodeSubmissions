#Author     : sakura_kyon@hotmail.com
#Question   : Reverse Nodes in k-Group
#Link       : https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
#Language   : python
#Status     : Accepted
#Run Time   : 316 ms
#Description: 
#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#You may not alter the values in the nodes, only nodes itself may be changed.
#Only constant memory is allowed.
#For example,
#Given this linked list: `1->2->3->4->5`
#For k = 2, you should return: `2->1->4->3->5`
#For k = 3, you should return: `3->2->1->4->5`

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def link_gen(head):
    while head:
        yield head
        head = head.next

def gen_link_up(gen):
    last = None
    head = None
    while 1:
        try:
            now = gen.next()
            if not head:
                head = now
            if last:
                last.next = now
            last = now
        except StopIteration:
            break
    return head

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None:
            return head
        lst = list()
        bu = list()
        for n in link_gen(head):
            bu.append(n)
            if len(bu) >= k:
                bu.reverse()
                lst.extend(bu)
                bu = list()
        if bu:
            lst.extend(bu)
        if len(lst) >= 2:
            for i in range(len(lst) - 1):
                lst[i].next = lst[i + 1]
            lst[-1].next = None
        return lst[0]