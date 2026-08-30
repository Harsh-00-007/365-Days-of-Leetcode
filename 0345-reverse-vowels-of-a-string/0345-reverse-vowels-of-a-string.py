class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use a set for O(1) lookup time
        vowels = set("aeiouAEIOU")
        
        # Convert string to list since strings are immutable in Python
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        while left < right:
            # Move left pointer until it hits a vowel
            if s_list[left] not in vowels:
                left += 1
            # Move right pointer until it hits a vowel
            elif s_list[right] not in vowels:
                right -= 1
            # Both pointers are at vowels, swap them
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        # Join the list back into a string
        return "".join(s_list)