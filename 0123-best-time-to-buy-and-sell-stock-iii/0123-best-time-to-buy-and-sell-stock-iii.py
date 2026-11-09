class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        ahead=[[0,0,0] for _ in range(2)]
        for index in range(n-1,-1,-1):
            curr=[[0,0,0] for _ in range(2)]
            for buy in range(0,2):
                for cap in range(1,3):
                    if buy==1:
                        buy_p = -prices[index] + ahead[0][cap] 
                        not_buy = 0 + ahead[1][cap]
                        profit=max(buy_p,not_buy)
                    else:
                        sell= prices[index] + ahead[1][cap-1]
                        not_sell = 0 + ahead[0][cap]
                        profit=max(sell,not_sell)
                    curr[buy][cap] = profit
            ahead=curr
        return ahead[1][2]