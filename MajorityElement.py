from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==e:
                count+=1
            else:
                count-=1
            if count==0:
                e=nums[i+1]
        return e
        
                

if __name__=='__main__':
    print(Solution().majorityElement([3,2,3]))