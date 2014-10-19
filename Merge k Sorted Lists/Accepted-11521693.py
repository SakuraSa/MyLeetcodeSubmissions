#Author     : sakura_kyon@hotmail.com
#Question   : Merge k Sorted Lists
#Link       : https://oj.leetcode.com/problems/merge-k-sorted-lists/
#Language   : python
#Status     : Accepted
#Run Time   : 568 ms
#Description: 
#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

def link_gen(head):
    while head:
        yield head
        head = head.next

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        lst = list()
        for head in lists:
            for i in link_gen(head):
                lst.append(i)
        if not lst:
            return None
        lst.sort(key=lambda n: n.val)
        return gen_link_up(iter(lst))