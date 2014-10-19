#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Inorder Traversal
#Link       : https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 96 ms
#Description: 
#Given a binary tree, return the inorder traversal of its nodes' values.
#For example:
#Given binary tree `{1,#,2,3}`,
#```
#   1
#    \
#     2
#    /
#   3
#```
#return `[1,3,2]`.
####Note:### Recursive solution is trivial, could you do it iteratively?
#confused what `"{1,#,2,3}"` means? [> read more on how binary tree is serialized on OJ.](#)
####OJ's Binary Tree Serialization:###
#The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
#Here's an example:
#```
#   1
#  / \
# 2   3
#    /
#   4
#    \
#     5
#```
#The above binary tree is serialized as `"{1,2,3,#,#,4,#,#,5}"`. 

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
    def inorderTraversal(self, root):
        return self.it(root, list())
        
    def it(self, root, an):
        if not root is None:
            self.it(root.left, an)
            an.append(root.val)
            self.it(root.right, an)
        return an
            
        