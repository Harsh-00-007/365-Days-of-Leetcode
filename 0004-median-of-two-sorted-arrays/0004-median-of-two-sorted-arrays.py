class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition index for nums1
            i = (low + high) // 2
            # Partition index for nums2
            j = (m + n + 1) // 2 - i
            
            # Boundary elements around the partitions
            max_left1 = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf') if i == m else nums1[i]
            
            max_left2 = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf') if j == n else nums2[j]
            
            # Check if partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total elements count is odd, return the maximum of left elements
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # If total elements count is even, return the average of max_left and min_right
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            elif max_left1 > min_right2:
                # We are too far right in nums1, move partition left
                high = i - 1
            else:
                # We are too far left in nums1, move partition right
                low = i + 1