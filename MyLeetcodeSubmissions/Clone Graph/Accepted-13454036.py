#Author     : sakura_kyon@hotmail.com
#Question   : Clone Graph
#Link       : https://oj.leetcode.com/problems/clone-graph/
#Language   : python
#Status     : Accepted
#Run Time   : 500 ms
#Description: 
#Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`.
####OJ's undirected graph serialization:###
#Nodes are labeled uniquely.
#We use `#` as a separator for each node, and `,` as a separator for node label and each neighbor of the node.
#As an example, consider the serialized graph `{0,1,2#1,2#2,2}`.
#The graph has a total of three nodes, and therefore contains three parts as separated by `#`.
#First node is labeled as0. Connect node0to both nodes1and2.Second node is labeled as1. Connect node1to node2.Third node is labeled as2. Connect node2to node2(itself), thus forming a self-cycle.
#Visually, the graph looks like the following:
#```
#       1
#      / \
#     /   \
#    0 --- 2
#         / \
#         \_/
#```
#Show Tags
#Depth-first SearchBreadth-first SearchGraph

#Code       : 
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

def travel(node):
    closed = set()
    opened = set()
    opened.add(node)
    while opened:
        n = opened.pop()
        closed.add(n)
        for nn in n.neighbors:
            if not nn in closed:
                opened.add(nn)
    return closed

def clone(node):
    nodes = list(travel(node))
    trans = {id(node): index for index, node in enumerate(nodes)}
    new_nodes = [UndirectedGraphNode(node.label) for node in nodes]
    for index, node in enumerate(new_nodes):
        node.neighbors = [new_nodes[trans[id(old_node)]] for old_node in nodes[index].neighbors]
    return new_nodes

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node:
            return sorted(list(clone(node)), key=lambda n: n.label)[0]
        else:
            return node
        