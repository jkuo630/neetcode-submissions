class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force -> sort -> keep a counter -> prev if prev = curr - 1 
        # iterate that 
        # o(n) 
        # o(nlogn) -> not optimal here 

        if len(nums) == 0:
            return 0 
        
        if len(nums) == 1:
            return 1

        nums.sort()
        ans = 1 
        curr = 1 

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1 
                ans = max(ans, curr)
            elif nums[i] != nums [i - 1]:
                curr = 1

        return ans 

        [0,1,1,2,2,3,3]

        # optimal -> 