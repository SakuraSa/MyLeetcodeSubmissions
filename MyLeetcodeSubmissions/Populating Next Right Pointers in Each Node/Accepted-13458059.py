#Author     : sakura_kyon@hotmail.com
#Question   : Populating Next Right Pointers in Each Node
#Link       : https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
#Language   : python
#Status     : Accepted
#Run Time   : 332 ms
#Description: 
#Given a binary tree
#```
#    struct TreeLinkNode {
#      TreeLinkNode *left;
#      TreeLinkNode *right;
#      TreeLinkNode *next;
#    }
#```
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
#Initially, all next pointers are set to `NULL`.
####Note:###
#* You may only use constant extra space.
#* You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
#For example,
#Given the following perfect binary tree,
#```
#         1
#       /  \
#      2    3
#     / \  / \
#    4  5  6  7
#```
#After calling your function, the tree should look like:
#```
#         1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \  / \
#    4->5->6->7 -> NULL
#```
#Show Tags
#TreeDepth-first Search

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            self.layer([root])
    
    def layer(self, roots):
        self.work(roots)
        nextLayer = list()
        for node in roots:
            if node.left:
                nextLayer.append(node.left)
            if node.right:
                nextLayer.append(node.right)
        if nextLayer:
            self.layer(nextLayer)
    
    def work(self, nodes):
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if nodes:
            nodes[-1].next = None
        