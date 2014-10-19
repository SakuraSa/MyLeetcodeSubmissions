#Author     : sakura_kyon@hotmail.com
#Question   : LRU Cache
#Link       : https://oj.leetcode.com/problems/lru-cache/
#Language   : python
#Status     : Accepted
#Run Time   : 1612 ms
#Description: 
#Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `set`.
#`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#`set(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

#Code       : 
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.ord = list()
        self.cap = capacity
        self.dic = dict()

    # @return an integer
    def get(self, key):
        if key in self.dic:
            self.use(key)
            return self.dic[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.use(key)
        self.dic[key] = value
        if len(self.ord) > self.cap:
            del self.dic[self.ord[-1]]
            del self.ord[-1]
            
            
    def use(self, key):
        if key in self.dic:
            self.ord.remove(key)
        self.ord.insert(0, key)
        
            