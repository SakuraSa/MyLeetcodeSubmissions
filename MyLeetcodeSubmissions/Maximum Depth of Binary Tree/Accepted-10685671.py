#Author     : sakura_kyon@hotmail.com
#Question   : Maximum Depth of Binary Tree
#Link       : https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 276 ms
#Description: 
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1