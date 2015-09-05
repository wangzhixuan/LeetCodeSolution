class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        best_profit = 0
        if len(prices)>0:
            lowest_price = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            elif prices[i] > prices[i-1] :
                profit = prices[i] - lowest_price
                best_profit = max(profit,best_profit)
            else:
                continue
        
        return best_profit    
            