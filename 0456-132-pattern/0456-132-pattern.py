class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []  # Monotonic stack storing candidates for '3' (nums[j])
        s3 = float('-inf')  # Value representing '2' (nums[k])

        # Traverse from right to left
        for num in reversed(nums):
            # If current num < s3, we found nums[i] < nums[k] < nums[j]
            if num < s3:
                return True
            
            # Maintain decreasing stack: update s3 to the largest valid '2'
            while stack and num > stack[-1]:
                s3 = stack.pop()
            
            # Push current element as a candidate for '3'
            stack.append(num)

        return False