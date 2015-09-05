"""
LeetCode OJ time: 56ms
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxSingleProfit(self, prices):
        """
        :param prices: a list of integers
        :return: a list of tuples (i, profit)
                 the best "profit" one can achieve before the "i"th day
                 by making a single buy and sell
        """
        best_profit = 0
        result = [[0, 0]]
        
        if len(prices) > 0:
            lowest_price = prices[0]
        
        for i in xrange(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            elif prices[i] > prices[i-1]:
                profit = prices[i] - lowest_price
                if profit > best_profit:
                    best_profit = profit
                    result.append((i,profit))
            else:
                continue
        
        return result

    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        
        profit1_list = self.maxSingleProfit(prices)
        if len(profit1_list) == 1: # monotonically decreasing price
            return 0
        
        profit1 = profit1_list.pop()

        best_profit2 = 0
        best_profit = profit1[1]

        highest_price = prices[-1]
        
        if profit1[0] == n-1:
            profit1 = profit1_list.pop()
        
        for i in xrange(n-2, 0, -1):
            """
            :profit1: is the best profit one can make with single buy and sell both before "i"th day
            :best_profit2: is the best profit one can make with single buy and sell both after "i"th day
            :best_profit: is the the total best profit one can achieve by 
            """
            if i == profit1[0]:
                profit1 = profit1_list.pop()
            
            if prices[i] > highest_price:
                highest_price = prices[i]
            elif prices[i] < prices[i+1]:
                profit = highest_price - prices[i]
                best_profit2 = max(profit, best_profit2)
                best_profit = max(best_profit, profit1[1] + best_profit2)
        
        return best_profit