from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       maxpro=0
       for i in range(len(prices)-1):
           if prices[i]<prices[i+1]:
               maxpro+=(prices[i+1]-prices[i])
       print(maxpro)
               

if __name__=='__main__':
    Solution().maxProfit([7,6,4,3,1])