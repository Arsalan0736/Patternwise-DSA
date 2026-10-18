class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b_price=prices[0]
        p=0
        for i in range(1,len(prices)):
            if prices[i]<b_price:
                b_price=prices[i]
            elif prices[i]-b_price > p:
                p = prices[i]-b_price
        return p