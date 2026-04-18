class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        t=[]
        for i in nums:
            t.append(i)

        nums=t+nums
        return(nums)

        