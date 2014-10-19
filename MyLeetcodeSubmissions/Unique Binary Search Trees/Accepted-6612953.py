#Author     : sakura_kyon@hotmail.com
#Question   : Unique Binary Search Trees
#Link       : https://oj.leetcode.com/problems/unique-binary-search-trees/
#Language   : python
#Status     : Accepted
#Run Time   : 152 ms
#Description: 
#Given n, how many structurally unique ###BST's### (binary search trees) that store values 1...n?
#For example,
#Given n = 3, there are a total of 5 unique BST's.
#```
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
#```

#Code       : 
class Solution:
    def __init__(self):
        self.mem = {0:1, 1:1}
    # @return an integer
    def numTrees(self, n):
        if n in self.mem:
            return self.mem[n]
        
        ret = 0
        for i in range(n):
            ret += self.numTrees(i) * self.numTrees(n - i - 1)
        self.mem[n] = ret
        return ret