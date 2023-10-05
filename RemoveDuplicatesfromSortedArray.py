from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[p]=nums[i]
                p+=1
        nums[p]=nums[i+1]

if __name__=='__main__':
    Solution().removeDuplicates([1,1,2])