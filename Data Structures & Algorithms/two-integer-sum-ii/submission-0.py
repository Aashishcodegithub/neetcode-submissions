class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashe={}
        for i in range(len(numbers)):
            need=target-numbers[i]
            if need in hashe:
                return[hashe[need]+1,i+1]
            hashe[numbers[i]]=i

        