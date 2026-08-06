class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        # Fill the result array from back to front with the larger square
        for pos in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
                
        return result