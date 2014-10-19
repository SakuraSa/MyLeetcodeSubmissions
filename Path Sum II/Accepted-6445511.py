#Author     : sakura_kyon@hotmail.com
#Question   : Path Sum II
#Link       : https://oj.leetcode.com/problems/path-sum-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 248 ms
#Description: 
#Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#For example:
#Given the below binary tree and `sum = 22`,
#```
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \    / \
#        7    2  5   1
#```
#return
#```
#[
#   [5,4,11,2],
#   [5,8,4,5]
#]
#```

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
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root:
            self.answers = list()
            self.ps(root, sum, [root.val])
            return self.answers
        else:
            return []
    
    def ps(self, root, sum, stack):
        if root is None:
            return
        n = sum - root.val
        if root.left is None and root.right is None and n == 0:
            self.answers.append(list(stack))
            return
        else:
            if root.left:
                stack.append(root.left.val)
                self.ps(root.left, n, stack)
                stack.pop()
            if root.right:
                stack.append(root.right.val)
                self.ps(root.right, n, stack)
                stack.pop()