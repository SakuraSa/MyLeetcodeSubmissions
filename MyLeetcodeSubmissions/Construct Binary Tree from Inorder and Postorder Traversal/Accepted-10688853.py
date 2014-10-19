#Author     : sakura_kyon@hotmail.com
#Question   : Construct Binary Tree from Inorder and Postorder Traversal
#Link       : https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 696 ms
#Description: 
#Given inorder and postorder traversal of a tree, construct the binary tree.
####Note:###
#You may assume that duplicates do not exist in the tree.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def buildTree(inorder, postorder):
    if not inorder:
        return None
    center = postorder.pop()
    ci = inorder.index(center)
    node = TreeNode(center)
    node.right = buildTree(inorder[ci+1:], postorder)
    node.left = buildTree(inorder[:ci], postorder)
    return node

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return buildTree(inorder, postorder)