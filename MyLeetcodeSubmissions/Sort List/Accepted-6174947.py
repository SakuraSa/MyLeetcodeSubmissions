#Author     : sakura_kyon@hotmail.com
#Question   : Sort List
#Link       : https://oj.leetcode.com/problems/sort-list/
#Language   : python
#Status     : Accepted
#Run Time   : 1924 ms
#Description: 
#Sort a linked list in O(n log n) time using constant space complexity.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
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
        