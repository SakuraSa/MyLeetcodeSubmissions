#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Level Order Traversal II
#Link       : https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 232 ms
#Description: 
#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#For example:
#Given binary tree `{3,9,20,#,#,15,7}`,
#```
#    3
#   / \
#  9  20
#    /  \
#   15   7
#```
#return its bottom-up level order traversal as:
#```
#[
#  [15,7],
#  [9,20],
#  [3]
#]
#```
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

def LTR(root):
    if root is None:
        return list()
    next_layer = [root]
    rs = list()
    while next_layer:
        rs.append([node.val for node in next_layer])
        layer = next_layer
        next_layer = list()
        for node in layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
    return rs

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        return LTR(root)[::-1]

        