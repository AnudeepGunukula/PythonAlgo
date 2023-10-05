from typing import List


class Solution:
    def reverse(self,nums,start,end):
        while start<=end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1


    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)   
        self.reverse(nums,0,len(nums)-k-1)
       
        self.reverse(nums,len(nums)-k,len(nums)-1)
        
        self.reverse(nums,0,len(nums)-1)
        

if __name__=='__main__':
    print(Solution().rotate([1,2,3,4,5,6,7],3))