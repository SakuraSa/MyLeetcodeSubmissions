#Author     : sakura_kyon@hotmail.com
#Question   : Candy
#Link       : https://oj.leetcode.com/problems/candy/
#Language   : python
#Status     : Accepted
#Run Time   : 572 ms
#Description: 
#There are N children standing in a line. Each child is assigned a rating value. 
#You are giving candies to these children subjected to the following requirements:
#* Each child must have at least one candy.
#* Children with a higher rating get more candies than their neighbors.
#What is the minimum candies you must give?

#Code       : 
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        length = len(ratings)
        candys = [0] * length
        works = list()
        
        for i in range(length):
            if i > 0 and ratings[i] > ratings[i - 1]:
                continue
            if i < length - 1 and ratings[i] > ratings[i + 1]:
                continue
            works.append(i)
            candys[i] = 1

        def sp(f, t):
            if t < 0 or t >= length:
                return
            if ratings[t] > ratings[f]:
                if candys[t] == 0 or candys[t] < candys[f] + 1:
                    candys[t] = candys[f] + 1
                    works.append(t)
        
        while works:
            index = works.pop()
            sp(index, index - 1)
            sp(index, index + 1)
                    
        return sum(candys)