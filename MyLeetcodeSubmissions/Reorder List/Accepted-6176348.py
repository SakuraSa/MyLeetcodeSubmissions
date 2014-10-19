#Author     : sakura_kyon@hotmail.com
#Question   : Reorder List
#Link       : https://oj.leetcode.com/problems/reorder-list/
#Language   : python
#Status     : Accepted
#Run Time   : 520 ms
#Description: 
#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#You must do this in-place without altering the nodes' values.
#For example,
#Given `{1,2,3,4}`, reorder it to `{1,4,2,3}`.

#Code       : 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        lst = list()
        while not head is None:
            lst.append(head)
            head = head.next
        
        tem = list()
        flag = True
        head, tail = 0, len(lst) - 1
        while head <= tail:
            if flag:
                tem.append(lst[head])
                head += 1
            else:
                tem.append(lst[tail])
                tail -= 1
            flag = not flag
        lst = tem
        
        for i in range(0, len(lst) - 1):
            lst[i].next = lst[i + 1]
        lst[len(lst) - 1].next = None
        return lst[0]