#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Postorder Traversal
#Link       : https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 152 ms
#Description: 
#Given a binary tree, return the postorder traversal of its nodes' values.
#For example:
#Given binary tree `{1,#,2,3}`,
#```
#   1
#    \
#     2
#    /
#   3
#```
#return `[3,2,1]`.
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
    def postorderTraversal(self, root):
        lst = list()
        if not root is None:
            self.pt(root, lst)
        return lst
        
    def pt(self, root, lst):
        if not root.left is None:
            self.pt(root.left, lst)
        if not root.right is None:
            self.pt(root.right, lst)
        lst.append(root.val)
