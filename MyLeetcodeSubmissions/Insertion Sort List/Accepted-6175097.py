#Author     : sakura_kyon@hotmail.com
#Question   : Insertion Sort List
#Link       : https://oj.leetcode.com/problems/insertion-sort-list/
#Language   : python
#Status     : Accepted
#Run Time   : 296 ms
#Description: 
#Sort a linked list using insertion sort.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        lst = list()
        while not head is None:
            lst.append((head.val, head))
            head = head.next
        lst.sort()
        for i in range(0, len(lst) - 1):
            lst[i][1].next = lst[i + 1][1]
        lst[len(lst) - 1][1].next = None
        return lst[0][1]