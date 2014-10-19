#Author     : sakura_kyon@hotmail.com
#Question   : Flatten Binary Tree to Linked List
#Link       : https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
#Language   : python
#Status     : Accepted
#Run Time   : 152 ms
#Description: 
#Given a binary tree, flatten it to a linked list in-place.
#For example,
#Given
#```
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6
#```
#The flattened tree should look like:
#```
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#```
#[click to show hints.](#)
####Hints:###
#If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        order = list()
        self.mt(root, order)
        self.relink(order)
    
    def mt(self, root, answer):
        if root is None:
            return
        answer.append(root)
        self.mt(root.left, answer)
        self.mt(root.right, answer)
    
    def relink(self, order):
        for i in range(len(order) - 1):
            order[i].left = None
            order[i].right = order[i + 1]
        if order:
            order[-1].left = order[-1].right = None