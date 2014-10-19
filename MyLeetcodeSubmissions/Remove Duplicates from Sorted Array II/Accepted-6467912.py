#Author     : sakura_kyon@hotmail.com
#Question   : Remove Duplicates from Sorted Array II
#Link       : https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 300 ms
#Description: 
#Follow up for "Remove Duplicates":
#What if duplicates are allowed at most twice?
#For example,
#Given sorted array A = `[1,1,1,2,2,3]`,
#Your function should return length = `5`, and A is now `[1,1,2,2,3]`.

#Code       : 
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        dic = dict()
        rm = list()
        most = 2
        
        for i in range(len(A)):
            c = A[i]
            dic[c] = dic.get(c, 0) + 1
            if dic[c] > most:
                rm.append(i)
        
        for i in rm[::-1]:
            del A[i]
        
        return len(A)