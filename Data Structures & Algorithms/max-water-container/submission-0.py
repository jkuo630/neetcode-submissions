class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left pointer 
        # right pointer 
        # move smaller one forwards 
        # until left < right 

        left = 0 
        right = len(heights) - 1 
        ans = 0 
        while left < right:
            area = min(heights[left], heights[right]) * ((right+1) - (left+1))
            ans = max(ans, area)
            if heights[left] < heights[right]:
                left += 1 
            elif heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1 
        
        return ans