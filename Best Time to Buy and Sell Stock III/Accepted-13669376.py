#Author     : sakura_kyon@hotmail.com
#Question   : Best Time to Buy and Sell Stock III
#Link       : https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#Language   : python
#Status     : Accepted
#Run Time   : 340 ms
#Description: 
#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete at most two transactions.
####Note:###
#You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#Show Tags
#ArrayDynamic Programming

#Code       : 
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        left_profit = []
        last = None
        profit = 0
        max_profit = 0
        for p in prices:
            if last is None:
                left_profit.append(0)
            else:
                profit = max(0, profit + p - last)
                max_profit = max(max_profit, profit)
                left_profit.append(max_profit)
            last = p
        right_profit = []
        last = None
        profit = 0
        max_profit = 0
        for p in reversed(prices):
            if last is None:
                right_profit.append(0)
            else:
                profit = max(0, profit + last - p)
                max_profit = max(max_profit, profit)
                right_profit.append(max_profit)
            last = p
        right_profit.reverse()
        return max(a + b for a, b in zip(left_profit, right_profit))