#Author     : sakura_kyon@hotmail.com
#Question   : Convert Sorted List to Binary Search Tree
#Link       : https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 484 ms
#Description: 
#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def listNode_gen(head):
    pt = head
    while pt:
        yield pt.val
        pt = pt.next

def BST(lst, fi=0, ti=None):
    if ti is None:
        ti = len(lst) - 1
    if fi > ti:
        return None
    ci = (fi + ti) / 2
    root = TreeNode(lst[ci])
    root.left = BST(lst, fi, ci - 1)
    root.right = BST(lst, ci + 1, ti)
    return root

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        return BST(list(listNode_gen(head)))
        
        