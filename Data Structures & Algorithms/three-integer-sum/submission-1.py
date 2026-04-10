class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for loop going thru all the nums 
        # two pointers going thru the numbers on the right, until target is met, or not 

        nums.sort()

        ans = []
        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1 
            right = len(nums) - 1 
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1 
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1 
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans 