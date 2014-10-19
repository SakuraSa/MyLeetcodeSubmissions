#Author     : sakura_kyon@hotmail.com
#Question   : Swap Nodes in Pairs
#Link       : https://oj.leetcode.com/problems/swap-nodes-in-pairs/
#Language   : python
#Status     : Accepted
#Run Time   : 144 ms
#Description: 
#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given `1->2->3->4`, you should return the list as `2->1->4->3`.
#Your algorithm should use only constant space. You may ###not### modify the values in the list, only nodes itself can be changed.

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
    def swapPairs(self, head, k=2):
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
        