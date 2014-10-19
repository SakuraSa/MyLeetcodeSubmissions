#Author     : sakura_kyon@hotmail.com
#Question   : Path Sum
#Link       : https://oj.leetcode.com/problems/path-sum/
#Language   : python
#Status     : Accepted
#Run Time   : 304 ms
#Description: 
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#For example:
#Given the below binary tree and `sum = 22`,
#```
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
#```
#return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        n = sum - root.val
        if root.left is None and root.right is None and n == 0:
            return True
        else:
            return self.hasPathSum(root.left, n) or self.hasPathSum(root.right, n)
            
        