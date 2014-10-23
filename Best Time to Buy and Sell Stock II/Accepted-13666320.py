#Author     : sakura_kyon@hotmail.com
#Question   : Best Time to Buy and Sell Stock II
#Link       : https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#Language   : python
#Status     : Accepted
#Run Time   : 252 ms
#Description: 
#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#Show Tags
#ArrayGreedy

#Code       : 
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        last = None
        for p in prices:
            if not last is None:
                profit += max(0, p - last)
            last = p
        return profit