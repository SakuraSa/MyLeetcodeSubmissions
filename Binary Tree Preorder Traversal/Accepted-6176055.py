#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Preorder Traversal
#Link       : https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 128 ms
#Description: 
#Given a binary tree, return the preorder traversal of its nodes' values.
#For example:
#Given binary tree `{1,#,2,3}`,
#```
#   1
#    \
#     2
#    /
#   3
#```
#return `[1,2,3]`.
####Note:### Recursive solution is trivial, could you do it iteratively?

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        lst = list()
        if not root is None:
            self.pt(root, lst)
        return lst
        
    def pt(self, root, lst):
        lst.append(root.val)
        if not root.left is None:
            self.pt(root.left, lst)
        if not root.right is None:
            self.pt(root.right, lst)
        