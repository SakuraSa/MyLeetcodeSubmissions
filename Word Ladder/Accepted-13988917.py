#Author     : sakura_kyon@hotmail.com
#Question   : Word Ladder
#Link       : https://oj.leetcode.com/problems/word-ladder/
#Language   : python
#Status     : Accepted
#Run Time   : 1588 ms
#Description: 
#Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#Only one letter can be changed at a timeEach intermediate word must exist in the dictionary
#For example,
#Given:
#start = `"hit"`
#end = `"cog"`
#dict = `["hot","dot","dog","lot","log"]`
#As one shortest transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`,
#return its length `5`.
####Note:###
#* Return 0 if there is no such transformation sequence.
#* All words have the same length.
#* All words contain only lowercase alphabetic characters.
#Show Tags
#Breadth-first Search

#Code       : 
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def ladderLength(self, start, end, words):
        char = [chr(c) for c in range(97, 123)]
        if not start or not end or not words or not len(start) or not len(words):
            return 0
        if start == end:
            return 0
        queue = collections.deque([(start, 1)]) 
        dist = set(start)
        while len(queue):
            word, dis = queue.popleft()
            dis += 1
            for i in range(len(word)):
                for c in char:
                    nw = word[:i] + c + word[i+1:]
                    if nw == end:
                        return dis 
                    if nw in words and nw not in dist:
                        queue.append([nw, dis])
                        dist.add(nw)
        return 0