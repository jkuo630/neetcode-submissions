class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # can iterate through each list, and do binary search on it 
        # o(n^2)
        def binarySearch(nums: List[int]) -> int:
            left = 0 
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1 
                else:
                    return mid
            
            return -1
        
        for lst in matrix:
            if binarySearch(lst) != -1:
                return True 
        
        return False

        # optimal solution -> binary search to correct list 
        # then binary search again within that list 