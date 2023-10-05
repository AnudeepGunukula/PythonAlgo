from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[p-2]:
                nums[p]=nums[i]
                p+=1

        print(nums)


if __name__=='__main__':
    Solution().removeDuplicates([1,1,1,2,2,3])