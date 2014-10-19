#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Maximum Path Sum
#Link       : https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
#Language   : python
#Status     : Accepted
#Run Time   : 840 ms
#Description: 
#Given a binary tree, find the maximum path sum.
#The path may start and end at any node in the tree.
#For example:
#Given the below binary tree,
#```
#       1
#      / \
#     2   3
#```
#Return `6`.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mem = dict()
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return -1000000000000000000000000000000000000000000000000
        max_this = root.val
        ps_left = self.maxPathSumFromRoot(root.left)
        if ps_left > 0:
            max_this += ps_left
        ps_right = self.maxPathSumFromRoot(root.right)
        if ps_right > 0:
            max_this += ps_right
        max_left = self.maxPathSum(root.left)
        max_right = self.maxPathSum(root.right)
        ret = max(max_this, max_left, max_right)
        #print root, ret
        return ret
    
    def maxPathSumFromRoot(self, root):
        if root is None:
            return 0
        ret = self.mem.get(id(root), None)
        if not ret is None:
            return ret
        ret_l = ret_r = root.val
        if root.left:
            ret_l += self.maxPathSumFromRoot(root.left) 
        if root.right:
            ret_r += self.maxPathSumFromRoot(root.right) 
        self.mem[id(root)] = ret = max(ret_l, ret_r, root.val)
        return ret
        
        