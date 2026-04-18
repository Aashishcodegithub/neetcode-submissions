class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        breath=len(heights)-1
        res=[]
        while left<right:
            a=min(heights[left],heights[right])
            res.append(a*breath)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            breath-=1
        return max(res)
        