class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Populate initial frequencies for s1 and first window of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # Count initial matching character frequencies (out of 26 English letters)
        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1

        # Slide the window across s2
        for i in range(n1, n2):
            if matches == 26:
                return True

            # Character entering the window on the right
            r = ord(s2[i]) - ord('a')
            s2_counts[r] += 1
            if s1_counts[r] == s2_counts[r]:
                matches += 1
            elif s1_counts[r] + 1 == s2_counts[r]:
                matches -= 1

            # Character leaving the window on the left
            l = ord(s2[i - n1]) - ord('a')
            s2_counts[l] -= 1
            if s1_counts[l] == s2_counts[l]:
                matches += 1
            elif s1_counts[l] - 1 == s2_counts[l]:
                matches -= 1

        return matches == 26