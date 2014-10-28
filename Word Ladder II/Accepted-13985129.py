#Author     : sakura_kyon@hotmail.com
#Question   : Word Ladder II
#Link       : https://oj.leetcode.com/problems/word-ladder-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 2240 ms
#Description: 
#Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#Only one letter can be changed at a timeEach intermediate word must exist in the dictionary
#For example,
#Given:
#start = `"hit"`
#end = `"cog"`
#dict = `["hot","dot","dog","lot","log"]`
#Return
#```
#  [
#    ["hit","hot","dot","dog","cog"],
#    ["hit","hot","lot","log","cog"]
#  ]
#```
####Note:###
#* All words have the same length.
#* All words contain only lowercase alphabetic characters.
#Show Tags
#ArrayBacktrackingBreadth-first SearchString

#Code       : 
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, words):
        #opened start & end into words
        words.add(start)
        words.add(end)
        #get edge
        edge = {word: [] for word in words}
        for word in words:
            for i in range(len(word)):
                for c in range(ord(word[i])+1, 123):
                    new_word = word[:i] + chr(c) + word[i+1:]
                    if new_word in words:
                        edge[word].append(new_word)
                        edge[new_word].append(word)
        #search
        pathes = []
        path_queue = collections.deque([[start]])
        closed = set([start])
        opened = []
        flag, size = 0, 1
        while len(path_queue):
            words = path_queue.popleft()
            if flag and len(words) >= flag:
                break
            if len(words) > size:
                size = len(words)
                closed |= set(opened)
                opened = []
            word = words[-1]
            for new_word in edge[word]:
                if new_word == end:
                    flag = len(words) + 1
                    pathes.append(words + [new_word])
                if new_word not in closed:
                    path_queue.append(words + [new_word])
                    opened.append(new_word)
        return pathes