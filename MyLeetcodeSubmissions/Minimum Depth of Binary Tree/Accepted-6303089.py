#Author     : sakura_kyon@hotmail.com
#Question   : Minimum Depth of Binary Tree
#Link       : https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 272 ms
#Description: 
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
    def minDepth(self, root):
        if root is None:
            return 0
        return self.md(root, 1, 10000000000)
        
    def md(self, root, depth, minDepth):
        if depth >= minDepth:
            return minDepth
        if root.left is None and root.right is None:
            return depth
        if root.left:
            minDepth = min(minDepth, self.md(root.left, depth + 1, minDepth))
        if root.right:
            minDepth = min(minDepth, self.md(root.right, depth + 1, minDepth))
        return minDepth
            