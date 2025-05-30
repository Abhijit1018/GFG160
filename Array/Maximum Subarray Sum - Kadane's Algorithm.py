class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        maxEnding = arr[0]
        
        for i in range(1,len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            res = max(res, maxEnding)
        return res


arr = [1,2,3,-2,5]
print(Solution().maxSubArraySum(arr))
