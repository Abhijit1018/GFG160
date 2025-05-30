class Solution:
    def maximumProfit(self, prices):
        minSofar = prices[0]
        res=0
        
        
        for i in range(1, len(prices)):
            minSofar = min(minSofar, prices[i])
            
            res = max(res, prices[i] - minSofar)
            
        return res
        
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maximumProfit(prices))
