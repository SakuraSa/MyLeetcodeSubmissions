#Author     : sakura_kyon@hotmail.com
#Question   : Copy List with Random Pointer
#Link       : https://oj.leetcode.com/problems/copy-list-with-random-pointer/
#Language   : python
#Status     : Accepted
#Run Time   : 680 ms
#Description: 
#A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#Return a deep copy of the list.

#Code       : 
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

def link_gen(head):
    while head:
        yield head
        head = head.next

def connnect(lst_gen):
    try:
        pnow = lst_gen.next()
        while 1:
            pnext = lst_gen.next()
            pnow.next = pnext
            pnow = pnext
    except StopIteration, e:
        pass
    

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        nlst = [RandomListNode(node.label) for node in link_gen(head)]
        connnect(iter(nlst))
        id_index_dict = {id(node):index for index, node in enumerate(link_gen(head))}
        for index, node in enumerate(link_gen(head)):
            if not node.random is None:
                nlst[index].random = nlst[id_index_dict[id(node.random)]]
        return nlst[0]
        