from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequencies of each character
        counts = Counter(s)
        
        # Build the result string
        res = []
        
        # most_common() sorts by frequency in descending order
        for char, freq in counts.most_common():
            res.append(char * freq)
            
        return "".join(res)