#Author     : sakura_kyon@hotmail.com
#Question   : Binary Tree Zigzag Level Order Traversal
#Link       : https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#Language   : python
#Status     : Accepted
#Run Time   : 180 ms
#Description: 
#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#For example:
#Given binary tree `{3,9,20,#,#,15,7}`,
#```
#    3
#   / \
#  9  20
#    /  \
#   15   7
#```
#return its zigzag level order traversal as:
#```
#[
#  [3],
#  [20,9],
#  [15,7]
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

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        nl = [root]
        ret = list()
        an = None
        depth = 0
        while nl:
            an, nl = self.zz(nl, depth)
            ret.append(an)
            depth += 1
        return ret
        
        
    def zz(self, roots, depth):
        flag = depth % 2 == 1
        if flag:
            order = roots[::-1]
        else:
            order = roots
        nl = list()
        an = list()
        for n in order:
            an.append(n.val)
        for n in roots:
            if n.left:
                nl.append(n.left)
            if n.right:
                nl.append(n.right)


        return an, nl
    
        