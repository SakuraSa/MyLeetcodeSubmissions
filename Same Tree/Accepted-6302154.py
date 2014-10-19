#Author     : sakura_kyon@hotmail.com
#Question   : Same Tree
#Link       : https://oj.leetcode.com/problems/same-tree/
#Language   : python
#Status     : Accepted
#Run Time   : 176 ms
#Description: 
#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

#Code       : 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        gp, gq = self.pt(p), self.pt(q)
        while True:
            np, nq = self.getNext(gp), self.getNext(gq)
            if np == nq == None:
                return True
            if np != nq:
                return False
        return True
        
    def getNext(self, g):
        try:
            return g.next()
        except StopIteration, e:
            return None
        
    def pt(self, root):
        if root is None:
            raise StopIteration()
        st = list()
        st.append((root, "root"))
        
        while st:
            t, name = st.pop()
            yield (t.val, name)
            if t.left:
                st.append((t.left, "left"))
            if t.right:
                st.append((t.right, "right"))
        
        raise StopIteration()
            