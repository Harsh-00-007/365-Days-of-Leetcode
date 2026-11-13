class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # If k >= 2, we can swap adjacent characters arbitrarily (bubble sort),
        # allowing us to reach the globally sorted string.
        if k >= 2:
            return "".join(sorted(s))
        
        # If k == 1, we can only generate cyclic shifts of the string.
        # Check all N rotations and return the lexicographically smallest.
        return min(s[i:] + s[:i] for i in range(len(s)))