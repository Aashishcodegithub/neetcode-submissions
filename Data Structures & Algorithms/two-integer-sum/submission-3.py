class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ts=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ts.append(i)
                    ts.append(j)
        return ts