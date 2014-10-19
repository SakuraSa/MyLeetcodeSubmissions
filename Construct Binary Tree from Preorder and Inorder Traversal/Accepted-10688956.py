#Author     : sakura_kyon@hotmail.com
#Question   : Construct Binary Tree from Preorder and Inorder Traversal
#Link       : https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 720 ms
#Description: 
#Given preorder and inorder traversal of a tree, construct the binary tree.
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
    node.left = buildTree(inorder[:ci], postorder)
    node.right = buildTree(inorder[ci+1:], postorder)
    return node

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return buildTree(inorder, preorder[::-1])