class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # double for loop 
        # pointer on one, -> next pointer iterates through the rest, looking for a num = to the diff 

        # i = 0 
        # while i < len(numbers):
        #     diff = target - numbers[i]
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[j] == diff:
        #             return [i + 1, j + 1]

        #     i += 1
        
        # two pointers, if sum is target than target, move right down, else, move left up 

        left = 0 
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1 
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]