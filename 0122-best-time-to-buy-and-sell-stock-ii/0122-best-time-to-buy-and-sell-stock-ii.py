class Solution:
    def solve(self,index,buy,prices,dp):
        if index == len(prices):
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]
        if buy==1:
            buy_p = -prices[index] + self.solve(index+1,0,prices,dp)
            not_buy = 0 + self.solve(index+1,1,prices,dp)
            profit=max(buy_p,not_buy)
        else:
            sell= prices[index] + self.solve(index+1,1,prices,dp)
            not_sell = 0 + self.solve(index+1,0,prices,dp)
            profit=max(sell,not_sell)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[-1,-1] for _ in range(n+1)]
        dp[n][0]=0
        dp[n][1]=0
        for index in range(n-1,-1,-1):
            for buy in range(0,2):
                if buy==1:
                    buy_p = -prices[index] + dp[index+1][0] 
                    not_buy = 0 + dp[index+1][1]
                    profit=max(buy_p,not_buy)
                else:
                    sell= prices[index] + dp[index+1][1]
                    not_sell = 0 + dp[index+1][0]
                    profit=max(sell,not_sell)
                dp[index][buy] = profit
        return dp[0][1]