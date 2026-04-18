class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=[]
        set(temp)
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                return True
        return False
