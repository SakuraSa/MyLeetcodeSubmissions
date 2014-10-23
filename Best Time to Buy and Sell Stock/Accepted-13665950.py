#Author     : sakura_kyon@hotmail.com
#Question   : Best Time to Buy and Sell Stock
#Link       : https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Language   : python
#Status     : Accepted
#Run Time   : 252 ms
#Description: 
#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        last = None
        profit = 0
        max_profit = 0
        for p in prices:
            if not last is None:
                profit = max(0, profit + p - last)
                max_profit = max(profit, max_profit)
            last = p
        return max_profit
            