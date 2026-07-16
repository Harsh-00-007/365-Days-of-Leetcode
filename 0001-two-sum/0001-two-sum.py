class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        harsh ={}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in harsh:
                return [i,harsh[remaining]]
            harsh[nums[i]] = i