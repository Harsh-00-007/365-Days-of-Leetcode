class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        
        # Loop while both 'a' and 'b' are remaining
        while a > 0 and b > 0:
            if a > b:
                ans.append("aab")
                a -= 2
                b -= 1
            elif b > a:
                ans.append("bba")
                a -= 1
                b -= 2
            else:  # a == b
                ans.append("ab")
                a -= 1
                b -= 1
                
        # Append remaining characters (at most 2 of 'a' or 'b')
        if a > 0:
            ans.append("a" * a)
        if b > 0:
            ans.append("b" * b)
            
        return "".join(ans)