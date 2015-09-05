"""
Leetcode OJ time: 60ms
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        bought = False
        profit = 0
        cost = 0
        
        if len(prices)<2:
            return 0
        
        for i in range(len(prices)):
            
            if i==0:
                buy = (prices[i] < prices[i+1])
                sell = False
            elif i==len(prices)-1:
                buy = False
                sell = bought and (prices[i] > prices[i-1])
            else:
                if bought:
                    buy =False
                    sell = (prices[i] >= prices[i+1]) and (prices[i]>=prices[i-1])
                else:
                    buy = (prices[i] <= prices[i+1]) and (prices[i]<=prices[i-1])
                    sell = False
            
            if buy:
                cost = prices[i]
                bought = True
            elif sell:
                profit += (prices[i] - cost)
                bought = False
            
        return profit