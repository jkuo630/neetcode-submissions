class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict -> [element, size]
        # sort dict based on size 
        # take first k elements 

        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        
        sorted_dict = sorted(elements.items(), key=lambda item: item[1], reverse=True)

        return_value = [item[0] for item in sorted_dict[:k]]

        return return_value
        