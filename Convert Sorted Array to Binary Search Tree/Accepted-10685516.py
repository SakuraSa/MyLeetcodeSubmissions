#Author     : sakura_kyon@hotmail.com
#Question   : Convert Sorted Array to Binary Search Tree
#Link       : https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 328 ms
#Description: 
#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return BST(num)