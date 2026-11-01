from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark visited numbers by negating the value at the corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Any index with a positive value means (index + 1) is missing
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
            else:
                # Restore the array back to original state (optional, good practice)
                nums[i] = -nums[i]
                
        return result