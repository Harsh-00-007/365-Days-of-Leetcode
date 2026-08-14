class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                # If this ')' immediately follows a '(', it is a leaf / core
                if s[i - 1] == '(':
                    score += 1 << depth  # equivalent to 2^depth
                    
        return score