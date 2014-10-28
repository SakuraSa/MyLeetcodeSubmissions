#Author     : sakura_kyon@hotmail.com
#Question   : Word Ladder II
#Link       : https://oj.leetcode.com/problems/word-ladder-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 2832 ms
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
    def findLadders(self, start, end, words):
        pathes=[]
        graphNodes={}
        queue=[(start,0,[])]
        minPath=0
        nodeShortPathCache={}
    
        while(len(queue)>0):
            node,dis,path=queue.pop(0)
    
            if(node not in graphNodes):
                    graphNodes[node]=[]
                    for i in range(len(node)):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            if(j==node[i]):
                                continue
                            newNode = node[0:i] + j + node[i + 1:]
                            if(newNode in words):
                                graphNodes[node].append(newNode)
    
            if(node in nodeShortPathCache):
                if(dis>nodeShortPathCache[node]):
                    continue
            else:
                nodeShortPathCache[node]=dis
            if(node==end):
                newpath=list(path)
                newpath.append(node)
                if(minPath==0):
                    minPath=dis
                if(dis==minPath):
                    pathes.append(newpath)
            else:
                newpath=list(path)
                newpath.append(node)
                for childNode in graphNodes[node]:
                    if(childNode in nodeShortPathCache):
                        if(dis+1>nodeShortPathCache[childNode]):
                            continue
                    queue.append((childNode,dis+1,newpath))
        return pathes