#Author     : sakura_kyon@hotmail.com
#Question   : Edit Distance
#Link       : https://oj.leetcode.com/problems/edit-distance/
#Language   : python
#Status     : Accepted
#Run Time   : 856 ms
#Description: 
#Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#You have the following 3 operations permitted on a word:
#a) Insert a character
#b) Delete a character
#c) Replace a character
#Show Tags
#Dynamic ProgrammingString

#Code       : 
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        d = [[0 for _ in xrange(n + 1)] for __ in xrange(m + 1)]
        for i in xrange(m+1):
            d[i][0] = i
        for i in xrange(n+1):
            d[0][i] = i
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = 1 + min(d[i-1][j], d[i-1][j-1], d[i][j-1])
        return d[m][n]