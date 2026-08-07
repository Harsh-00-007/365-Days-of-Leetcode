class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_len = 0
        i = 1
        
        while i < n - 1:
            # Check if index i is a valid peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand left
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                # Expand right
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                # Calculate current mountain length
                mountain_len = right - left + 1
                max_len = max(max_len, mountain_len)
                
                # Move pointer to the end of the current mountain
                i = right
            else:
                i += 1
                
        return max_len