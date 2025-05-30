from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i]>prices[i - 1]:
                res += prices[i]-prices[i - 1]
                
        
        return res
        
if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(Solution().maximumProfit(prices))

