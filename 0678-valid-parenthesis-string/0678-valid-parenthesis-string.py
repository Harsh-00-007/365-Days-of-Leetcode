class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible open '(' count
        cmax = 0  # Maximum possible open '(' count

        for char in s:
            if char == "(":
                cmin += 1
                cmax += 1
            elif char == ")":
                cmin -= 1
                cmax -= 1
            elif char == "*":
                cmin -= 1  # If '*' is ')'
                cmax += 1  # If '*' is '('

            # Too many ')' encountered
            if cmax < 0:
                return False

            # cmin cannot drop below 0 (an asterisk can act as empty)
            if cmin < 0:
                cmin = 0

        # Valid if we can end with exactly 0 open parentheses
        return cmin == 0