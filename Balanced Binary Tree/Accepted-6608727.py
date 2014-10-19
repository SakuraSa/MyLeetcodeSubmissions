#Author     : sakura_kyon@hotmail.com
#Question   : Balanced Binary Tree
#Link       : https://oj.leetcode.com/problems/balanced-binary-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 488 ms
#Description: 
#Given a binary tree, determine if it is height-balanced.
#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        if root.left and not self.isBalanced(root.left):
            return False
        if root.right and not self.isBalanced(root.right):
            return False
        return abs(self.treeDepth(root.left) - self.treeDepth(root.right)) <= 1
    
    mem = dict()
    def treeDepth(self, root):
        if root in self.mem:
            return self.mem[root]
        if root is None:
            dp = 0
        else:
            dp = max(self.treeDepth(root.left), self.treeDepth(root.right)) + 1
        self.mem[root] = dp
        return dp
        