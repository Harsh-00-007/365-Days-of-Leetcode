class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        
        for i in range(0, n, 2 * k):
            # Reverse the first k characters of the current 2k block
            chars[i : i + k] = reversed(chars[i : i + k])
            
        return "".join(chars)