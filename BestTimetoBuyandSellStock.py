from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro=0
        min=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            maxpro=max(maxpro,prices[i]-min)
        print(maxpro)


if __name__=='__main__':
    Solution().maxProfit([7,6,4,3,1])