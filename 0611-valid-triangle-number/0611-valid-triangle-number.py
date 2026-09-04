class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side k from right to left
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                # If nums[i] + nums[j] > nums[k], then every index from i to j-1
                # paired with j will also be greater than nums[k] because the array is sorted.
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1

        return count