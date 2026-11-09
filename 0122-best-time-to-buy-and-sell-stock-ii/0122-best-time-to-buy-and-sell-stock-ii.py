class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        ahead=[0,0] 
        
        for index in range(n-1,-1,-1):
            curr=[-1,-1]
            for buy in range(0,2):
                if buy==1:
                    buy_p = -prices[index] + ahead[0] 
                    not_buy = 0 + ahead[1]
                    profit=max(buy_p,not_buy)
                else:
                    sell= prices[index] + ahead[1]
                    not_sell = 0 + ahead[0]
                    profit=max(sell,not_sell)
                curr[buy] = profit
            ahead=curr
        return ahead[1]